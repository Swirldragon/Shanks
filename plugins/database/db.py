import datetime
import mysql.connector
from mysql.connector import Error
import pymysql
from loguru import logger
import sqlite3

conn = sqlite3.connect('user_data.db')

class Database:
    def __init__(self):
        timeout = 10
        self.connection = pymysql.connect(
            charset="utf8mb4",
            connect_timeout=timeout,
            cursorclass=pymysql.cursors.DictCursor,
            db="defaultdb",
            host="shanks-justatestsubject-c98a.h.aivencloud.com",
            password="AVNS_uxSiv4oYViwH83p8Lbe",
            read_timeout=timeout,
            port=26463,
            user="avnadmin",
            write_timeout=timeout,
        )
        self.cursor = self.connection.cursor()  # Initialize cursor here
        self.create_table_if_not_exists()
        
    def create_table_if_not_exists(self):
        try:
            self.cursor.execute("""
                                CREATE TABLE IF NOT EXISTS users (
                                user_id INTEGER PRIMARY KEY,
                                thumbnail BLOB,
                                file_caption TEXT,
                                email TEXT,
                                password TEXT
                                )
                                """)
            self.connection.commit()
        except pymysql.Error as e:
            logger(f"Error: {e}")
                                
    def new_user(self, id):
        return {
            'id': id,
            'join_date': datetime.date.today().isoformat(),
            'apply_caption': False,
            'upload_as_doc': False,
            'thumbnail': None,
            'caption': None
        }

    def add_user(self, id):
        user = self.new_user(id)
        self.cursor.execute("INSERT INTO users (id, join_date, apply_caption, upload_as_doc, thumbnail, caption) VALUES (%s, %s, %s, %s, %s, %s)", (user['id'], user['join_date'], user['apply_caption'], user['upload_as_doc'], user['thumbnail'], user['caption']))
        self.connection.commit()

    def is_user_exist(self, id):
        self.cursor.execute("SELECT * FROM users WHERE id=%s", (id,))
        return bool(self.cursor.fetchone())

    def total_users_count(self):
        self.cursor.execute("SELECT COUNT(*) FROM users")
        return self.cursor.fetchone()[0]

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
        self.connection.commit()

    def set_apply_caption(self, id, apply_caption):
        self.cursor.execute("UPDATE users SET apply_caption=%s WHERE id=%s", (apply_caption, id))
        self.connection.commit()

    def get_apply_caption(self, id):
        self.cursor.execute("SELECT apply_caption FROM users WHERE id=%s", (id,))
        return self.cursor.fetchone()[0]

    def set_upload_as_doc(self, id, upload_as_doc):
        self.cursor.execute("UPDATE users SET upload_as_doc=%s WHERE id=%s", (upload_as_doc, id))
        self.connection.commit()

    def get_upload_as_doc(self, id):
        self.cursor.execute("SELECT upload_as_doc FROM users WHERE id=%s", (id,))
        return self.cursor.fetchone()[0]

    def set_thumbnail(self, id, thumbnail):
        self.cursor.execute("UPDATE users SET thumbnail=%s WHERE id=%s", (thumbnail, id))
        self.connection.commit()

    def get_thumbnail(self, id):
        self.cursor.execute("SELECT thumbnail FROM users WHERE id=%s", (id,))
        return self.cursor.fetchone()[0]

    def set_caption(self, id, caption):
        self.cursor.execute("UPDATE users SET caption=%s WHERE id=%s", (caption, id))
        self.connection.commit()

    def get_caption(self, id):
        self.cursor.execute("SELECT caption FROM users WHERE id=%s", (id,))
        return self.cursor.fetchone()[0]

    def get_user_data(self, id):
        self.cursor.execute("SELECT * FROM users WHERE id=%s", (id,))
        return self.cursor.fetchone()

db = Database()
