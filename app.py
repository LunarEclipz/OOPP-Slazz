from flask import Flask, render_template
from forms import transfer_form, topup_form
app = Flask(__name__)

app.config["SECRET_KEY"] = 'b54f94e1090e5a348f355adb5a59334e'

@app.route('/pay')
def pay():
    return render_template("pay.html", title="Pay")

# Transfer Tab
@app.route('/transfer', methods=["GET", "POST"])
def transfer():
    form1 = transfer_form()
    form2 = topup_form()
    return render_template("transfer.html", title="Transfer", form1=form1, form2=form2)

@app.route('/transactions')
def transactions():
    return render_template("transactions.html", title="Transactios")

@app.route('/add')
def add():
    return render_template("add.html", title="Add")

if __name__ == '__main__':
    app.run(debug=True)



