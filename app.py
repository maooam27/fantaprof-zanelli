from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def homepage():
    name = ""
    if request.method == 'POST':
        name = request.form.get('prof')
    print(name)
    return render_template('index.html')


app.run(debug=True)
