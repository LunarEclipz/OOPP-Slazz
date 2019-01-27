from flask import *
import payment_data
import update_log
import shelve
from functools import wraps


app = Flask(__name__)
app.config["SECRET_KEY"] = 'b54f94e1090e5a348f355adb5a59334e'

# Main Tab
@app.route('/')
def pay():
    db = payment_data
    bdb = shelve.open('log.db')
    return render_template('pay.html', title='Pay', db=db, bdb=bdb)

# Top-up Tab
@app.route('/pay/topup')
def topup():
    db = payment_data
    bdb = shelve.open('log.db')
    return render_template("top_up.html", title="Top-Up", db=db, bdb=bdb)

# Transaction Tab
@app.route('/pay/transactions', methods=['POST', 'GET'])
def transactions():
    db = payment_data
    bdb = shelve.open('log.db')
    try:
        if request.method == 'POST':
            result = request.form
            amount = result['amount']
            try:
                name = result['name']
                p = update_log.Update(name, amount)
                p.amount = amount
                p.name = name
            except:
                p = update_log.topup(amount)
                p.amount = amount
                p.name = p.get_name()
            db = payment_data
            db.add_info('Bob', p)
            bdb = shelve.open('log.db')
            return render_template("transactions.html", title="Transactions", result=result, db=db, bdb=bdb)
    except:
        db = payment_data
        bdb = shelve.open('log.db')
    return render_template("transactions.html", title="Transactions", db=db, bdb=bdb)


# Add Tab
@app.route('/pay/add')
def add():

    return render_template("add.html", title="Add")

if __name__ == '__main__':
    app.run(debug=True)



