import sqlite3

database = sqlite3.connect('database.db')
cursor = database.cursor()

cursor.execute(f'''UPDATE Punti SET UltimaAzione = {action}''')
