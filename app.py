from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def homepage():
    name = ""
    action = ""
    if request.method == 'POST':
        name = request.form.get('prof')
        action = request.form.get('action')
    print(name, action)
    return render_template('index.html')


app.run(debug=True)
