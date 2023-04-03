import sqlite3;

con = sqlite3.connect("metanit.db")
cursor = con.cursor()

# создаем таблицу people
cursor.execute("""CREATE TABLE people
                (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                name TEXT, 
                age INTEGER)
            """)