def calculate_budget(income, medical_expense, children_age_groups, credit_score, debt, housing_input=None, total_transportation=0, qualifies_for_assistance=False, education_expense=0):
    # Children costs based on age groups
    cost_per_child = {
        'young_children': {'food': 0.03, 'clothing': 0.01, 'medical': 0.02, 'education': 0.01, 'childcare': 0.05, 'transport': 0.02, 'entertainment': 0.01},
        'school_age_children': {'food': 0.04, 'clothing': 0.02, 'medical': 0.01, 'education': 0.02, 'childcare': 0.02, 'transport': 0.03, 'entertainment': 0.02},
        'teenagers': {'food': 0.06, 'clothing': 0.03, 'medical': 0.02, 'education': 0.03, 'childcare': 0, 'transport': 0.05, 'entertainment': 0.03}
    }
    
    # Calculate total children expenses based on age groups
    children_expense = 0
    for age_group, count in children_age_groups.items():
        for category, percentage in cost_per_child[age_group].items():
            children_expense += percentage * count * income

    # Food (base + children expenses)
    food = 0.15 * income + children_expense
    
    # Utilities
    utilities = 0.10 * income
    
    # Housing (user input or default calculation)
    if housing_input is not None:
        housing = housing_input  # User input takes precedence
    else:
        housing = min(0.30 * income, 2000)  # Default calculation if no input
    
    # Transportation (total input value instead of breakdown)
    transportation = total_transportation  # Direct user input for total transportation
    
    # Insurance
    insurance = 0.05 * income
    
    # If qualifies for government assistance, adjust expenses
    if qualifies_for_assistance:
        medical_expense = 0  # Assume medical expenses are covered
        food = food * 0.75  # Assume food expenses are reduced by 25% due to assistance
    
    # Debt Payments
    debt_payments = 0.10 * income + (debt / income * 0.05 * income)
    if credit_score >= 600:
        debt_payments -= ((credit_score - 600) / (850 - 600)) * 0.03 * income
    
    # Savings Calculation based on desired savings percentage
    savings = 0.20 * income - (debt / income * 0.10 * income)
    
    # Adding Education Expenses
    total_education_expenses = education_expense + (children_age_groups.get('school_age_children', 0) * 0.02 * income)  # Assume extra for school-age kids
    
    # Disposable Income
    disposable_income = income - (food + utilities + housing + medical_expense + 
                                  transportation + insurance + debt_payments + savings + total_education_expenses)
    
    # Output dictionary
    budget = {
        'Food': food,
        'Utilities': utilities,
        'Housing': housing,
        'Medical Expenses': medical_expense,
        'Transportation': transportation,
        'Insurance': insurance,
        'Debt Payments': debt_payments,
        'Savings': savings,
        'Education Expenses': total_education_expenses,
        'Disposable Income': disposable_income
    }
    
    return budget