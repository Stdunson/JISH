import os
from dotenv import load_dotenv
import openai
import pyttsx3
import re

load_dotenv()

# Load API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Assume these variables are set by the frontend
income = None
debtAmount = None
medicalExpensesAmount = None
numberOfChildren = None
foodSpending = None
utilitySpending = None
housingSpending = None
debtSpending = None
transportationSpending = None

# Option to enable or disable text-to-speech
enable_text_to_speech = True

# Create the prompt for OpenAI
prompt = (
    f"User's monthly income is {income} dollars. "
    f"Total monthly debt amount is {debtAmount} dollars. "
    f"Monthly medical expenses are {medicalExpensesAmount} dollars. "
    f"User has {numberOfChildren} children. "
    f"Monthly food spending is {foodSpending} dollars. "
    f"Monthly utility spending is {utilitySpending} dollars. "
    f"Monthly housing spending is {housingSpending} dollars. "
    f"Monthly debts spending is {debtSpending} dollars. "
    f"Monthly transportation spending is {transportationSpending} dollars. "
    "Provide budgeting advice on how to spend on the following categories: food, utility, housing, disposable income, savings, insurance, and debts."
)

try:
    chat_completion = openai.ChatCompletion.create(
        messages=[
            {
                "role": "system",
                "content": "You are a financial advisor helping an illiterate person with budgeting.",
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4o",
        api_key=api_key
    )

    response_text = chat_completion.choices[0].message.content

    # Preprocess the response text to remove hashtags and asterisks
    cleaned_response_text = re.sub(r'[#*]', '', response_text)

    # Summarize the response
    summary_prompt = (
        "Summarize the following response in one paragraph using simple English:\n\n"
        f"{cleaned_response_text}"
    )

    summary_completion = openai.ChatCompletion.create(
        messages=[
            {
                "role": "system",
                "content": "You are an academic summarizer.",
            },
            {
                "role": "user",
                "content": summary_prompt,
            }
        ],
        model="gpt-4o",
        api_key=api_key
    )

    summary_text = summary_completion.choices[0].message.content
    print("Summarized Response:")
    print(summary_text)

    if enable_text_to_speech:
        # Initialize the text-to-speech engine
        engine = pyttsx3.init()

        # Set properties for the voice
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  # Change index to select a different voice
        engine.setProperty('rate', 150)  # Speed of speech
        engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

        engine.say(summary_text)
        engine.runAndWait()

    # Extract budget categories and amounts from the response text
    budget_categories = ["food", "utility", "housing", "disposable income", "savings", "insurance", "debts"]
    
    # Initialize variables to store budget values
    food_budget = None
    utility_budget = None
    housing_budget = None
    disposable_income_budget = None
    savings_budget = None
    insurance_budget = None
    debts_budget = None

    budget_values = []

    for category in budget_categories:
        match = re.search(rf"{category}.*?(\d+)", cleaned_response_text, re.IGNORECASE)
        if match:
            budget_values.append(int(match.group(1)))
        else:
            budget_values.append(0) 

    # Assign budget values to variables
    food_budget, utility_budget, housing_budget, disposable_income_budget, savings_budget, insurance_budget, debts_budget = budget_values

    # Output the budget values and percentages
    total_budget = sum(budget_values)
    for category, value in zip(budget_categories, budget_values):
        percentage = (value / total_budget) * 100 if total_budget > 0 else 0
        print(f"{category.capitalize()}: {value} dollars ({percentage:.2f}%)")

    # Check if the user qualifies for government assistance
    qualifies_for_assistance = income < 2152

    if qualifies_for_assistance:
        print("You may qualify for government assistance. Please try again if confirm that it applies.")   

except openai.error.OpenAIError as e:
    print(f"An error occurred: {e}")
