import sqlite3

def delete_all_rows_in_jobs_table(db_path='./jobs.db'):
    """Deletes all rows from the jobs table in the SQLite database."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM jobs")
        conn.commit()

        print("All rows in the jobs table have been deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error occurred: {e}")
    finally:
        if conn:
            conn.close()

delete_all_rows_in_jobs_table()