import os
from dotenv import load_dotenv
import openai
import pyttsx3
import re
import matplotlib.pyplot as plt

load_dotenv()

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),  # Load API key from environment variable
)

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
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a financial advisor.",
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4o",
    )

    response_text = chat_completion.choices[0].message.content
    print(response_text)

    # Preprocess the response text to remove hashtags and asterisks
    cleaned_response_text = re.sub(r'[#*]', '', response_text)

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties for the voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Change index to select a different voice
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

    engine.say(cleaned_response_text)
    engine.runAndWait()

    # Extract budget categories and amounts from the response text
    budget_categories = ["food", "utility", "housing", "disposable income", "savings", "insurance", "debts"]
    budget_values = []

    for category in budget_categories:
        match = re.search(rf"{category}.*?(\d+)", cleaned_response_text, re.IGNORECASE)
        if match:
            budget_values.append(int(match.group(1)))
        else:
            budget_values.append(0)

    # Generate pie chart
    plt.figure(figsize=(10, 7))
    plt.pie(budget_values, labels=budget_categories, autopct='%1.1f%%', startangle=140)
    plt.title('Suggested Budget Distribution')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

    # Check if the user qualifies for government assistance
    qualifies_for_assistance = income < 2152

    if qualifies_for_assistance:
        print("You may qualify for government assistance. Please try again if confirm that it applies.")

except openai.error.OpenAIError as e:
    print(f"An error occurred: {e}")