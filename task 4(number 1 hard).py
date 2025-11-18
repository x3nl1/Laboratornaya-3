class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.is_connected = False
        return cls._instance
    
    def connect(self):
        if not self.is_connected:
            self.is_connected = True
            return "Подключено к базе данных"
        return "Уже подключено"
    
    def disconnect(self):
        if self.is_connected:
            self.is_connected = False
            return "Отключено от базы данных"
        return "Уже отключено"

db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1.connect())
print(db2.connect())
print(f"db1 is db2: {db1 is db2}")
