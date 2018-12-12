from flask import Flask, render_template, url_for, flash, redirect
from forms import SurveyForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route('/')
def Financehome():
    return render_template("Finance.html", title='Finance')


@app.route('/Survey', methods=['GET', 'POST'])
def Survey():
    form = SurveyForm()
    if form.validate_on_submit():
        flash(f'F&B: {form.f_budget.data}\n Essential: {form.e_budget.data}\n Leisure: {form.l_budget.data}\n Others: {form.o_budget.data} Submitted!', 'success')
        return redirect(url_for('Advisor'))
    return render_template("Survey.html", title='Survey', form=form)


saved_data = [{'Month': 'September', 'Amount': 20, 'Anno': 'Sep'},
              {'Month': 'October', 'Amount': 30, 'Anno': 'Oct'},
              {'Month': 'November', 'Amount': 40, 'Anno': 'Oct'},
              {'Month': 'December', 'Amount': 20, 'Anno': 'Oct'}]


@app.route('/Savings')
def Savings():
    return render_template("Savings.html", title='Savings', saved_data=saved_data)


spending_data = [{'Department': 'Food and Beverages', 'Amount': 25},
                 {'Department': 'Essentials', 'Amount': 75},
                 {'Department': 'Leisure', 'Amount': 225},
                 {'Department': 'Others', 'Amount': 100}]


@app.route('/Spending')
def Spending():
    return render_template("Spending.html", title='Spending', spending_data=spending_data)


@app.route('/Advisor')
def Advisor():
    return render_template("Advisor.html", title='Advisor',  spending_data=spending_data)


activities = [{'Name': 'Lazer Tag', 'Price': 30, 'Open': '3 to 5pm', 'Picture': 'https://cdn.getyourguide.com/img/tour_img-661869-148.jpg'},
              {'Name': 'Game of Tag', 'Price': 3, 'Open': '1 to 5pm', 'Picture': 'data:image/jpeg;base64,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'}]


@app.route('/Activity')
def Activity():
    return render_template("Activity.html", title='Activity', activities=activities)


if __name__ == '__main__':
    app.run()
