import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self):
        self.sql_create_notes_table = """CREATE TABLE IF NOT EXISTS notes(
                                         id integer PRIMARY KEY,
                                         name text NOT NULL,
                                         notes text NOT NULL
                                         );"""
        self.sql_create_tables = [self.sql_create_notes_table]

    def create_table(self, conn, create_table_sql):
        """
        Creates database tables if they do not exist.

        :param conn: sql connection
        :param create_table_sql: tables to create with sqlite.
        :return: None
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
            conn.close()
        except Error as e:
            print(e)

    def create_connection(self, db_file):
        """
        creates the database.db file.

        :param db_file: file path to the database.
        :return: conn: this is the database connection that is created when the function runs.
        """
        print("creating db connection")
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("connected to db")
            # return conn
        except Error as e:
            print(e)

        return conn

    def add_note(self, conn, user_data):
        """
        adds a note for the user to the database.

        :param conn:  opened database object.
        :param user_data: tuple containing the the name of the note, and the contents of the note.
        :return: True
        """
        print("add note called.")
        sql = '''INSERT INTO notes(name, notes)
        VALUES(?,?)'''
        cur = conn.cursor()
        cur.execute(sql, user_data)
        conn.commit()
        conn.close()
        return True

    def get_user_notes(self, conn):
        """
        queries the database for notes associated with the user_id from the users table.

        :param conn: opened database object
        :param user_id: this is the user id associated with this table from the users table.
        :return: rows: these are the notes added by a given user.
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM notes")
        rows = cur.fetchall()
        conn.close()
        return rows

    def edit_note(self, conn, note_to_edit):
        sql = '''UPDATE notes
                 SET name = ?,
                     notes = ?
                 WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql, note_to_edit)
        conn.commit()