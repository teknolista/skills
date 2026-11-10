import androidx.room.migration.Migration
import androidx.sqlite.db.SupportSQLiteDatabase

val NOTES_1_TO_2 = object : Migration(1, 2) {
    override fun migrate(database: SupportSQLiteDatabase) {
        database.execSQL("ALTER TABLE notes ADD COLUMN pinned INTEGER NOT NULL DEFAULT 0")
    }
}
