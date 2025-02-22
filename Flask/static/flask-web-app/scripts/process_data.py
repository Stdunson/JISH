def process_input(data):
    # Convert relevant values to integers
    processed_data = {}
    for key, value in data.items():
        if key in ["monthlyIncome", "creditScore", "debtSpending", "foodSpending", "utilitySpending", "housingSpending", "savingsSpending", "insuranceSpending", "transportationSpending"]:
            processed_data[key] = int(value) if value else 0
        else:
            processed_data[key] = value
    return processed_data