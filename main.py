from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def Financehome():
    return render_template("Finance.html")


@app.route('/Survey.html')
def Survey():
    return render_template("Survey.html")


if __name__ == '__main__':
    app.run()
