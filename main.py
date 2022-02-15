from Person import *
import actions
import sqlite3

database = sqlite3.connect('database.db')
cursor = database.cursor()

soragni = Prof("Soragni", 0, "Fisica")
magliani = Prof("Magliani", 0, "Informatica")
caroli = Prof("Caroli", 0, "Matematica")
domenico = Prof("Domenico", 0, "Biologia")
curcuruto = Prof("Curcuruto", 0, "Chimica")
fontana = Prof("Fontana", 0, "Inglese")
viani = Prof("Viani", 0, "Motoria")
mantovani = Prof("Mantovani", 0, "Arte")
rosa = Prof("Rosa", 0, "AutoCAD")
peluso = Prof("Peluso", 0, "Religione")
roberto = Prof("Roberto", 0, "Italiano")

database.execute(f"""INSERT INTO Punti (ID, Nome, UltimaAzione, UltimiPunti, Materia, PuntiTotali, DataUltima) 
VALUES (null, '{soragni.name}', 'azione placeholder', 69, '{soragni.subject}',
0, datetime('now', 'localtime'))""")

database.commit()
