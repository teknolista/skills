import base64
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPT=Path(__file__).resolve().parents[1]/'publish_quiz.py'
spec=importlib.util.spec_from_file_location('quiz',SCRIPT)
quiz=importlib.util.module_from_spec(spec);spec.loader.exec_module(quiz)

class QuizTests(unittest.TestCase):
    def fixture(self):
        return {'questions':[{'question':'Why this cache?', 'options':['retain data','lose data','skip errors','disable auth'], 'correct':0,'explanation':'Keep observed records.'}]}
    def load(self,data):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'q.json';p.write_text(json.dumps(data));return quiz.load_quiz(p)
    def test_shuffled_key_matches_visible_correct_option(self):
        with patch.object(quiz.random,'shuffle',lambda values:values.reverse()):
            ident,block=quiz.render(self.load(self.fixture()))
        key=block.split('<!-- pr-quiz-key:')[1].split(' -->')[0]
        decoded=json.loads(base64.b64decode(key))
        self.assertEqual(decoded['id'],ident)
        self.assertEqual(decoded['answers'],{'1':'D'})
        self.assertIn('- [ ] **D)** retain data',block)
    def test_boolean_correct_is_rejected(self):
        data=self.fixture();data['questions'][0]['correct']=True
        with self.assertRaises(ValueError):self.load(data)
    def test_nontext_or_duplicate_options_rejected(self):
        for options in [['a',5],[' a ','a']]:
            data=self.fixture();data['questions'][0]['options']=options
            with self.assertRaises(ValueError):self.load(data)
    def test_malformed_schema_rejected(self):
        for data in [[],{}, {'questions':[]},{'questions':[1]}]:
            with self.assertRaises(ValueError):self.load(data)
    def test_replacement_preserves_outside_text_and_backslashes(self):
        body='Maintainer note\n'+quiz.START+'\nold\n'+quiz.END+'\nDo not lose this.'
        block=quiz.START+'\nnew \\1\n'+quiz.END
        actual=quiz.replace_quiz(body,block)
        self.assertEqual(actual,'Maintainer note\n'+block+'\nDo not lose this.')
    def test_ambiguous_markers_refuse_modification(self):
        for body in [quiz.START,quiz.END,quiz.END+quiz.START,quiz.START+quiz.START+quiz.END]:
            with self.assertRaises(ValueError):quiz.replace_quiz(body,'new')
    def test_markup_in_question_cannot_end_quiz_block(self):
        data=self.fixture();data['questions'][0]['question']=quiz.END+'\n<script>question</script>'
        _,block=quiz.render(self.load(data))
        self.assertEqual(block.count(quiz.END),1)
        self.assertNotIn('<script>',block)
    def test_question_and_options_render_as_literal_text(self):
        data=self.fixture()
        data['questions'][0]['question']='Why [this](https://example.test) @reviewer `code`?'
        data['questions'][0]['options'][0]='![preview](https://example.test/image.png)'
        _,block=quiz.render(self.load(data))
        self.assertNotIn('[this](',block)
        self.assertNotIn('@reviewer',block)
        self.assertNotIn('![preview](',block)
        self.assertIn('&#64;reviewer',block)
    def test_dry_run_never_invokes_github(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'quiz.json';p.write_text(json.dumps(self.fixture()))
            with patch.object(sys,'argv',['publish_quiz.py','123',str(p),'--dry-run']), patch.object(quiz.subprocess,'run',side_effect=AssertionError('No GitHub call expected')), patch('builtins.print'):
                quiz.main()

if __name__=='__main__':unittest.main()
