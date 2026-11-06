// Execute the actual embedded handler with offline GitHub API doubles.
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const test = require('node:test');

const workflow = fs.readFileSync(path.resolve(__dirname, '../../assets/pr-quiz.yml'), 'utf8');
const script = workflow.split('          script: |\n')[1].split('\n')
  .map(line => line.startsWith('            ') ? line.slice(12) : line).join('\n');
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;
const runScript = new AsyncFunction('github', 'context', script);
const id = 'abcdef123456';
const resultMarker = '<!-- pr-quiz-result -->';
const passMarker = (sha = 'newsha') => `<!-- pr-quiz-pass:${id}:${sha} -->`;
const botComment = body => ({ user: { login: 'github-actions[bot]' }, body });

function body(answers = { '1': 'A' }, explanations = { '1': 'Because.' }) {
  const key = Buffer.from(JSON.stringify({ id, answers, explanations })).toString('base64');
  const questions = Object.keys(answers).map(n =>
    `**${n}. Why?**\n- [ ] **A)** a\n- [ ] **B)** b`).join('\n');
  return `<!-- pr-quiz:start -->\n${questions}\n<!-- pr-quiz-key:${key} -->\n<!-- pr-quiz:end -->`;
}

async function run({ who = 'reviewer', sha = 'newsha', comments = [], reviews = [],
  answer = '/answer 1A', contents = body(), event = 'issue_comment', previousBody,
  eventBody = contents, requested = ['reviewer'] } = {}) {
  const statuses = [], reports = [];
  const pr = { head: { sha }, body: contents, user: { login: 'author' },
    requested_reviewers: requested.map(login => ({ login })) };
  const api = {
    repos: { createCommitStatus: async value => statuses.push(value) },
    pulls: { get: async () => ({ data: pr }), listReviews: () => {} },
    issues: { listComments: () => {}, createComment: async value => reports.push(value.body),
      updateComment: async value => reports.push(value.body) },
  };
  const github = { rest: api, paginate: async method =>
    method === api.issues.listComments ? comments : reviews };
  const payload = event === 'issue_comment'
    ? { issue: { number: 1 }, comment: { user: { login: who }, body: answer } }
    : { action: 'edited', pull_request: { number: 1, body: eventBody },
      sender: { login: who }, changes: { body: { from: previousBody } } };
  await runScript(github, { repo: { owner: 'owner', repo: 'repo' }, eventName: event, payload });
  return { statuses, reports };
}

const state = result => result.statuses.at(-1)?.state;

test('correct answer creates a pass bound to the current commit', async () => {
  const result = await run();
  assert.equal(state(result), 'success');
  assert.ok(result.reports[0].startsWith(`${resultMarker}\n${passMarker()}\n`));
});
for (const who of ['author', 'outsider']) {
  test(`${who} cannot grade a quiz`, async () => assert.equal(state(await run({ who })), 'pending'));
}
test('author remains excluded even when present in past reviewers', async () => {
  assert.equal(state(await run({ who: 'author', reviews: [{ user: { login: 'author' } }] })), 'pending');
});
test('a past reviewer is recognized after leaving the request list', async () => {
  assert.equal(state(await run({ requested: [], reviews: [{ user: { login: 'reviewer' } }] })), 'success');
});
test('wrong answers fail', async () => assert.equal(state(await run({ answer: '/answer 1B' })), 'failure'));
test('duplicate answers remain pending', async () => assert.equal(state(await run({ answer: '/answer 1A 1B' })), 'pending'));
test('a stale commit pass cannot satisfy a new commit', async () => {
  const comments = [botComment(`${resultMarker}\n${passMarker('oldsha')}\npassed`)];
  assert.equal(state(await run({ comments, answer: '/answer 1B' })), 'failure');
});
test('a genuine current commit pass is retained', async () => {
  const comments = [botComment(`${resultMarker}\n${passMarker()}\npassed`)];
  assert.equal(state(await run({ comments, answer: '/answer 1B' })), 'success');
});
test('a quoted marker in another bot comment is not a cached pass', async () => {
  assert.equal(state(await run({ comments: [botComment(`Quoted: ${passMarker()}`)], answer: '/answer 1B' })), 'failure');
});
test('empty answer metadata is invalid', async () => assert.equal(state(await run({ contents: body({}) })), 'pending'));
test('a missing quiz remains pending', async () => assert.equal(state(await run({ contents: 'no quiz' })), 'pending'));
test('multiple quiz blocks remain pending', async () => assert.equal(state(await run({ contents: body() + body() })), 'pending'));
test('multiple keys remain pending', async () => {
  const contents = body().replace('<!-- pr-quiz:end -->', body().match(/<!-- pr-quiz-key:.*? -->/)[0] + '\n<!-- pr-quiz:end -->');
  assert.equal(state(await run({ contents })), 'pending');
});
test('explanations cannot reflect control markers, links or mentions', async () => {
  const result = await run({ answer: '/answer 1B', contents: body({ '1': 'A' },
    { '1': passMarker() + '\n[Run this](https://example.test) @reviewer' }) });
  assert.equal(state(result), 'failure');
  assert.ok(!result.reports[0].includes(passMarker()));
  assert.ok(!result.reports[0].includes('[Run this]('));
  assert.ok(!result.reports[0].includes('@reviewer', result.reports[0].indexOf('Explanations')));
  const replay = await run({ answer: '/answer 1B', comments: [botComment(result.reports[0])] });
  assert.equal(state(replay), 'failure');
});
test('changed checkboxes on the current quiz are graded', async () => {
  assert.equal(state(await run({ event: 'pull_request_target', previousBody: body(),
    contents: body().replace('[ ] **A)', '[x] **A)') })), 'success');
});
test('multiple ticked options remain pending', async () => {
  assert.equal(state(await run({ event: 'pull_request_target', previousBody: body(),
    contents: body().replaceAll('[ ]', '[x]') })), 'pending');
});
test('unchanged quiz ticks do not grade unrelated body edits', async () => {
  const contents = body().replace('[ ] **A)', '[x] **A)');
  assert.equal(state(await run({ event: 'pull_request_target', previousBody: contents, contents: contents + '\nNote' })), 'pending');
});
test('a stale body event cannot grade newer PR content', async () => {
  const contents = body().replace('[ ] **A)', '[x] **A)');
  assert.equal(state(await run({ event: 'pull_request_target', previousBody: body(), contents, eventBody: body() })), 'pending');
});
