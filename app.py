from flask import Flask, request, render_template
from actions import *
from Person import *
import sqlite3


app = Flask(__name__)


def insert_db(prof: Prof, azione: str, punti: int):
    database = sqlite3.connect('database.db')
    cursor = database.cursor()

    final_total = None

    # fetch
    cursor.execute(f"""SELECT PuntiTotali FROM Punti WHERE Nome = '{prof.name}'""")
    initial_total = cursor.fetchall()

    for row in initial_total:
        final_total = row

    cursor.execute(f'''UPDATE Punti SET UltimaAzione = "{azione}", UltimiPunti = {punti},
    PuntiTotali = {punti + final_total[0]}, DataUltima = CURRENT_TIME WHERE Nome = "{prof.name}"''')

    # database.execute(f"""INSERT INTO Punti (ID, Nome, UltimaAzione, UltimiPunti, Materia, PuntiTotali, DataUltima)
    # VALUES (null, '{prof.name}', '{azione}', {punti}, '{prof.subject}', {punti},
    # datetime('now', 'localtime'))""")
    database.commit()
    print(initial_total)


def get_points(action):
    if action == "assenza":
        return assenza()
    elif action == "parolaccia":
        return parolaccia()
    elif action == "scriveAllaLavagna":
        return scriveAllaLavagna()
    elif action == "capriolaSullaCattedra":
        return capriolaSullaCattedra()
    elif action == "maloreInClasse":
        return maloreInClasse()
    elif action == "portaInGita":
        return portaInGita()
    elif action == "inciampa":
        return inciampa()
    elif action == "risata":
        return risata()
    elif action == "mostraCapezzoli":
        return mostraCapezzoli()
    elif action == "relax":
        return relax()
    elif action == "gergoGiovanile":
        return gergoGiovanile()
    elif action == "correzioneImmediata":
        return correzioneImmediata()
    elif action == "defecazioneInClasse":
        return defecazioneInClasse()
    elif action == "complimento":
        return complimento()
    elif action == "nonFunzionaComputer":
        return nonFunzionaComputer()
    elif action == "esercitazione":
        return esercitazione()
    elif action == "vesteMonocromo":
        return vesteMonocromo()
    elif action == "sbagliaNome":
        return sbagliaNome()
    elif action == "perGiornoDopo":
        return perGiornoDopo()
    elif action == "nota":
        return nota()
    elif action == "pois":
        return pois()
    elif action == "supplente":
        return supplente()
    elif action == "apreRobe":
        return apreRobe()
    elif action == "catastrofe":
        return catastrofe()
    elif action == "pianto":
        return pianto()
    elif action == "litiga":
        return litiga()
    elif action == "ritardo":
        return ritardo()
    elif action == "battuta":
        return battuta()
    elif action == "dimenticaVerifiche":
        return dimenticaVerifiche()
    elif action == "positivo":
        return positivo()
    elif action == "insultaPercula":
        return insultaPercula()
    elif action == "tocca":
        return tocca()
    elif action == "lavoroGruppo":
        return lavoroGruppo()
    elif action == "nonMandaBagno":
        return nonMandaBagno()


def commit__to_database(name, action):
    """
    Commits the data to the database
    VALUES = (name, action)
    """

    prof = Prof(name, 0, None)
    punti = get_points(action)

    insert_db(prof, action, punti)


@app.route('/', methods=['GET', 'POST'])
def homepage():
    name = ""
    action = ""
    if request.method == 'POST':
        name = request.form.get('prof')
        action = request.form.get('action')
        commit__to_database(name, action)
        print(name, action)
    return render_template('index.html')


app.run(debug=True)
