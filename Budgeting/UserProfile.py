import sqlite3
import math
import re

def create_userprofile_table(con):
    try:
        cur = con.cursor()
        # Create the userprofile table if it doesn't exist
        cur.execute('''CREATE TABLE IF NOT EXISTS userprofile (
                    username TEXT PRIMARY KEY,
                    income REAL,
                    medexpenses REAL,
                    childcare REAL,
                    credscore INTEGER,
                    housingcost REAL,
                    transportcost REAL,
                    foodcost REAL,
                    electric REAL,
                    water REAL,
                    internet REAL,
                    savings REAL,
                    insurance REAL,
                    debt REAL)''')
        con.commit()
    except sqlite3.Error as e:
        print(f"Error creating userprofile table: {e}")

def profile_exists(con, username):
    try:
        cur = con.cursor()
        cur.execute('SELECT 1 FROM userprofile WHERE username = ?', (username,))
        return cur.fetchone() is not None
    except sqlite3.Error as e:
        print(f"Error checking if profile exists: {e}")
        return False

def collect_profile_data(con, username, income, insurance, medical_expenses, young_children, school_aged_children, teenagers, debt, housing_taxes, electricity_bill, water_bill, internet_bill):
    try:
        cur = con.cursor()
        # Insert the collected data into the userprofile table
        cur.execute('''INSERT INTO userprofile (
                        username, income, medexpenses, childcare, credscore, housingcost, transportcost, foodcost, electric, water, internet, savings, insurance, debt)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (username, income, medical_expenses, young_children + school_aged_children + teenagers, 0, housing_taxes, 0, 0, electricity_bill, water_bill, internet_bill, 0, insurance, debt))

        # Commit the changes
        con.commit()
    except sqlite3.Error as e:
        print(f"Error collecting profile data: {e}")

def display_user_info(con, username):
    try:
        cur = con.cursor()
        cur.execute('SELECT * FROM userprofile WHERE username = ?', (username,))
        user_info = cur.fetchone()
        if user_info:
            print("User Profile Information:")
            print(f"Income: {user_info[1]}")
            print(f"Medical Expenses: {user_info[2]}")
            print(f"Childcare: {user_info[3]}")
            print(f"Credit Score: {user_info[4]}")
            print(f"Housing Cost: {user_info[5]}")
            print(f"Transport Cost: {user_info[6]}")
            print(f"Food Cost: {user_info[7]}")
            print(f"Electric: {user_info[8]}")
            print(f"Water: {user_info[9]}")
            print(f"Internet: {user_info[10]}")
            print(f"Savings: {user_info[11]}")
            print(f"Insurance: {user_info[12]}")
            print(f"Debt: {user_info[13]}")
        else:
            print("No profile information found for this user.")
            if input("Would you like to register your profile information now? (yes/no): ").strip().lower() == "yes":
                income = float(input("Enter your monthly income: "))
                insurance = float(input("Enter your total monthly insurance expenses: "))
                medical_expenses = float(input("Enter your monthly medical expenses: "))

                # Ask if the user has children in each category
                young_children = 0
                school_aged_children = 0
                teenagers = 0

                if input("Do you have young children? (yes/no): ").strip().lower() == "yes":
                    young_children = int(input("Enter the number of young children you have: "))

                if input("Do you have school-aged children? (yes/no): ").strip().lower() == "yes":
                    school_aged_children = int(input("Enter the number of school-aged children you have: "))

                if input("Do you have teenagers? (yes/no): ").strip().lower() == "yes":
                    teenagers = int(input("Enter the number of teenagers you have: "))

                debt = float(input("Enter your total debt: "))
                housing_taxes = float(input("Enter your monthly housing taxes: "))

                # Collect utility expenses
                electricity_bill = float(input("Enter your monthly electricity bill: "))
                water_bill = float(input("Enter your monthly water bill: "))
                internet_bill = float(input("Enter your monthly internet bill: "))

                collect_profile_data(con, username, income, insurance, medical_expenses, young_children, school_aged_children, teenagers, debt, housing_taxes, electricity_bill, water_bill, internet_bill)
    except sqlite3.Error as e:
        print(f"Error displaying user info: {e}")

# Connect to the database
try:
    con = sqlite3.connect('userlogin.db')
    create_userprofile_table(con)
except sqlite3.Error as e:
    print(f"Error connecting to the database: {e}")
finally:
    if con:
        con.close()

