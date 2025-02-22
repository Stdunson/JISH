from flask import Blueprint, render_template, request, redirect, url_for
from scripts.process_data import process_input

main = Blueprint('main', __name__)

# Landing Page Route (Starting Page)
@main.route('/', methods=['GET'])
def index():
    return render_template('landing.html')  # Show landing page first

# Sign-in Route (Redirects to Form Page)
@main.route('/signin', methods=['POST'])
def signin():
    username = request.form.get("username")
    password = request.form.get("password")

    # TODO: Add authentication logic if needed

    return redirect(url_for('main.form_page'))  # Redirect to form page

# Form Page Route
@main.route('/form', methods=['GET'])
def form_page():
    return render_template('form.html')  # Render the form page

# Submit Route (Processes User Input)
@main.route('/submit', methods=['POST'])
def submit():
    user_data = {
        "monthlyIncome": request.form.get("monthlyIncome"),
        "creditScore": request.form.get("creditScore"),
        "hasDebt": request.form.get("hasDebt") == "on",
        "debtSpending": request.form.get("debtSpending"),
        "hasMedicalExpenses": request.form.get("hasMedicalExpenses") == "on",
        "foodSpending": request.form.get("foodSpending"),
        "utilitySpending": request.form.get("utilitySpending"),
        "housingSpending": request.form.get("housingSpending"),
        "savingsSpending": request.form.get("savingsSpending"),
        "insuranceSpending": request.form.get("insuranceSpending"),
        "transportationSpending": request.form.get("transportationSpending"),
    }

    pieChartValues = process_input(user_data)
    return redirect(url_for('main.dashboard', **pieChartValues))

# Dashboard Route
@main.route('/dashboard')
def dashboard():
    result = request.args.to_dict()
    return render_template('dashboard.html', data=result)
