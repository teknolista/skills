# Export queue contract

`service.queue_export` is the real entry point in this fixture. A document owner may queue one export and gets 202. A signed-in user who does not own a known document receives 403 and must not create a queue item. A nonexistent document returns 404 with no queued work. An existing queue item remains intact on a rejected call. The queue is a plain Python list and the project uses Python's built-in unittest runner. There are no external dependencies.
