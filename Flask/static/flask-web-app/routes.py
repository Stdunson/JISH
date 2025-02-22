from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from scripts.process_data import process_input

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    return render_template('form.html')  # Render the form when the user visits the site

@main.route('/submit', methods=['POST'])
def submit():
    # Collect all form inputs
    user_data = {
        "monthlyIncome": request.form.get("monthlyIncome"),
        "creditScore": request.form.get("creditScore"),
        "hasDebt": request.form.get("hasDebt") == "on",  # Checkbox returns "on" if checked
        "debtSpending": request.form.get("debtSpending"),
        "hasMedicalExpenses": request.form.get("hasMedicalExpenses") == "on",
        "foodSpending": request.form.get("foodSpending"),
        "utilitySpending": request.form.get("utilitySpending"),
        "housingSpending": request.form.get("housingSpending"),
        "savingsSpending": request.form.get("savingsSpending"),
        "insuranceSpending": request.form.get("insuranceSpending"),
        "transportationSpending": request.form.get("transportationSpending"),
    }

    # Process the data using your Python function
    pieChartValues = process_input(user_data)

    # Redirect to the dashboard with the processed result as query parameters
    return redirect(url_for('main.dashboard', **pieChartValues))

@main.route('/dashboard')
def dashboard():
    # Extract the processed data from query parameters
    result = request.args.to_dict()
    return render_template('dashboard.html', data=result)