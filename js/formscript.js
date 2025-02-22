//toggling the text boxes
function toggleDebtInput() {
    const debtInputContainer = document.getElementById('debtInputContainer');
    if (document.getElementById('hasDebt').checked) {
        debtInputContainer.innerHTML = `
            <label for="debtAmount">Debt Amount:</label>
            <input type="number" id="debtAmount" name="debtAmount" required>
        `;
    } else {
        debtInputContainer.innerHTML = '';
    }
}

function toggleMedicalExpensesInput() {
    const medicalExpensesInputContainer = document.getElementById('medicalExpensesInputContainer');
    if (document.getElementById('hasMedicalExpenses').checked) {
        medicalExpensesInputContainer.innerHTML = `
            <label for="medicalExpensesAmount">Medical Expenses Amount:</label>
            <input type="number" id="medicalExpensesAmount" name="medicalExpensesAmount" required>
        `;
    } else {
        medicalExpensesInputContainer.innerHTML = '';
    }
}

function toggleChildrenInput() {
    const childrenInputContainer = document.getElementById('childrenInputContainer');
    if (document.getElementById('hasChildren').checked) {
        childrenInputContainer.innerHTML = `
            <label for="numberOfChildren">Number of Children:</label>
            <input type="number" id="numberOfChildren" name="numberOfChildren" required>
        `;
    } else {
        childrenInputContainer.innerHTML = '';
    }
}

// Next Button
function nextStep(step) {
    const currentStepNumber = step - 1;
    if (checkStepValid(currentStepNumber)) {
        const currentStep = document.querySelector('.form-step:not([style*="display: none"])');
        currentStep.style.display = 'none';
        document.getElementById(`step${step}`).style.display = 'block';
    } else {
        alert('Incorrect Input');
    }
}

// Prev Button
function prevStep(step) {
    const currentStep = document.querySelector('.form-step:not([style*="display: none"])');
    currentStep.style.display = 'none';
    document.getElementById(`step${step}`).style.display = 'block';
}

//checking each step
function checkStepValid(step){
    const moneySteps = [1, 6, 7, 8, 9, 10, 11, 12];
    const boxSteps = [2, 3, 4];
    const numSteps = [2, 5];

    if(moneySteps.includes(step)){
        console.log("Doing step # "+ step);
        if(document.getElementById(`step${step}`).querySelector('input').value === ''){
            return false;
        }
        if(document.getElementById(`step${step}`).querySelector('input').value < 0){
            return false;
        }
    }

    if(boxSteps.includes(step)){
        console.log("Doing step # "+ step);
        if(document.getElementById(`step${step}`).querySelector('input').checked){
            if(document.getElementById(`step${step}`).querySelector('input').value === ''){
                return false;
            }
            if(document.getElementById(`step${step}`).querySelector('input').value < 0){
                return false;
            }
        }
    }

    if(numSteps.includes(step)){
        console.log("Doing step # "+ step);
        if(step === 2){
            if(document.getElementById(`step${step}`).querySelector('input').value < 300 || document.getElementById(`step${step}`).querySelector('input').value > 850){
                return false;
            }
        }else{
            if(document.getElementById(`step${step}`).querySelector('input').value < 0){
                return false;
            }
        }
    }

    return true;
}

//collecting input values
function collectInputValues() {
    const income = document.getElementById('monthlyIncome').value;
    const creditScore = document.getElementById('creditScore').value;
    const hasDebt = document.getElementById('hasDebt').checked;
    let debtAmount;
    const hasMedicalExpenses = document.getElementById('hasMedicalExpenses').checked;
    let medicalExpensesAmount;
    const hasChildren = document.getElementById('hasChildren').checked;
    let numberOfChildren;
    const foodSpending = document.getElementById('foodSpending').value;
    const utilitySpending = document.getElementById('utilitySpending').value;
    const housingSpending = document.getElementById('housingSpending').value;
    const savingsSpending = document.getElementById('savingsSpending').value;
    const insuranceSpending = document.getElementById('insuranceSpending').value;
    const debtSpending = document.getElementById('debtSpending').value;
    const transportationSpending = document.getElementById('transportationSpending').value;

    if(!hasDebt) {
        debtAmount = 0;
    }else{
        debtAmount = document.getElementById('debtAmount').value;
    }
    if(!hasMedicalExpenses) {
        medicalExpensesAmount = 0;
    }else{
        medicalExpensesAmount = document.getElementById('medicalExpensesAmount').value;
    }
    if(!hasChildren) {
        numberOfChildren = 0;
    }else{
        numberOfChildren = document.getElementById('numberOfChildren').value;
    }

    return {
        income,
        creditScore,
        debtAmount,
        medicalExpensesAmount,
        numberOfChildren,
        foodSpending,
        utilitySpending,
        housingSpending,
        savingsSpending,
        insuranceSpending,
        debtSpending,
        transportationSpending
    };
}

//button submit
const inputValues = [];
const submitButton = document.getElementById('submitButton');


function handleSubmit(event){
    event.preventDefault();
    inputValues.push(collectInputValues());
    alert(JSON.stringify(inputValues));
}

//sending data to flask
async function sendData() {
    try {
        const response = await fetch('http://localhost:5000/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(inputValues)
        });
        const data = await response.json();
        console.log('Success:', data);
    } catch (error) {
        console.error('Error:', error);
    }
}