
import sqlite3
from typing import List, Dict, Any

class Table:    
    def __init__(self, db_name: str = "database.db"):
        self.db_name = db_name
        self._create_connection()
    
    def _create_connection(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
    
    def create_table(self, table_name: str, columns: Dict[str, str]):
        columns_def = ", ".join([f"{name} {type_}" for name, type_ in columns.items()])
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_def})"
        
        self.cursor.execute(sql)
        self.connection.commit()
        print(f"Таблица {table_name} создана или уже существует")
    
    def insert(self, table_name: str, data: Dict[str, Any]) -> int:
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?" for _ in data])
        values = list(data.values())
        
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        
        self.cursor.execute(sql, values)
        self.connection.commit()
        
        last_id = self.cursor.lastrowid
        print(f"Данные добавлены в таблицу {table_name}, ID: {last_id}")
        return last_id
    
    def select(self, table_name: str, columns: List[str] = None, 
               where: str = None, params: tuple = None) -> List[Dict]:
        if columns is None:
            columns = ["*"]
        
        columns_str = ", ".join(columns)
        sql = f"SELECT {columns_str} FROM {table_name}"
        
        if where:
            sql += f" WHERE {where}" 
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        
        column_names = [description[0] for description in self.cursor.description]
        
        results = []
        for row in self.cursor.fetchall():
            results.append(dict(zip(column_names, row)))     
        return results
    
    def close(self):
        self.connection.close()

def demo_orm():
    orm = Table("test.db")
    
    users_columns = {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "TEXT NOT NULL",
        "age": "INTEGER",
        "email": "TEXT"
    }
    orm.create_table("users", users_columns)
    
    user1_id = orm.insert("users", {
        "name": "Иван Петров",
        "age": 28,
        "email": "ivan@mail.com"
    })
    
    user2_id = orm.insert("users", {
        "name": "Анна Сидорова",
        "age": 32,
        "email": "anna@mail.com"
    })
    
    user3_id = orm.insert("users", {
        "name": "Петр Иванов",
        "age": 24,
        "email": "petr@mail.com"
    })
    
    all_users = orm.select("users")
    print("Все пользователи:")
    for user in all_users:
        print(user)
    
    older_users = orm.select("users", where="age > ?", params=(27,))
    print("\nПользователи старше 26 лет:")
    for user in older_users:
        print(user)
    
    orm.close()

demo_orm()
