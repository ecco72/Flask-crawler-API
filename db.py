import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "flask.db")    #sqlite3需要指定路徑
conn = sqlite3.connect(db_path, check_same_thread=False)
cursor = conn.cursor()