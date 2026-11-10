# Migration planning fixture

The production change is in `NotesMigration.kt`. The application uses Room. Its Android build and test runner are absent from this fixture. Existing version 1 databases store user-authored notes. Preserve them when planning the version 2 migration test.
