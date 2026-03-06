import sqlite3
import datetime

class Database:
    def __init__(self, db_name="daily_bot.db"):
        """Инициализация базы данных"""
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()
    
    def create_tables(self):
        """Создание таблиц"""
        
        # Таблица пользователей
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                last_name TEXT,
                registered_date TEXT,
                timezone INTEGER DEFAULT 3
            )
        ''')
        
        # Таблица задач/событий
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                title TEXT NOT NULL,
                description TEXT,
                task_date TEXT NOT NULL,
                task_time TEXT,
                reminder_time INTEGER DEFAULT 30,
                is_completed INTEGER DEFAULT 0,
                is_notified INTEGER DEFAULT 0,
                created_at TEXT,
                category TEXT DEFAULT 'личное',
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        ''')
        
        # Таблица категорий
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                category_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                name TEXT NOT NULL,
                color TEXT DEFAULT '#3498db',
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        ''')
        
        # Таблица напоминаний
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS reminders (
                reminder_id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_id INTEGER,
                reminder_time TEXT NOT NULL,
                sent INTEGER DEFAULT 0,
                FOREIGN KEY (task_id) REFERENCES tasks (task_id)
            )
        ''')
        
        self.conn.commit()