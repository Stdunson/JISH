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

function inputIsValid(){
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

    if(creditScore === '' || income === '' || debtAmount === '' || medicalExpensesAmount === '' || numberOfChildren === ''){
        return false;
    }
    if(creditScore < 300 || creditScore > 850){
        return false;
    }
    if(income < 0 || debtAmount < 0 || medicalExpensesAmount < 0 || numberOfChildren < 0){
        return false;
    }

    if(foodSpending === '' || utilitySpending === '' || housingSpending === '' || savingsSpending === '' || insuranceSpending === '' || debtSpending === '' || transportationSpending === ''){
        return false;
    }
    if(foodSpending < 0 || utilitySpending < 0 || housingSpending < 0 || savingsSpending < 0 || insuranceSpending < 0 || debtSpending < 0 || transportationSpending < 0){
        return false;
    }

    if(foodSpending > income || utilitySpending > income || housingSpending > income || savingsSpending > income || insuranceSpending > income || debtSpending > income){
        return false;
    }


    return true;

}   

//button submit
const inputValues = [];
const submitButton = document.getElementById('submitButton');


function handleSubmit(event){
    event.preventDefault();
    if(inputIsValid()){
        inputValues.push(collectInputValues());
        alert(JSON.stringify(inputValues));
    }else{
        console.log('Invalid input');
        alert('Invalid input');
    }
}

//sending data
async function sendData() {
    let input = inputValues;
}

//recieving data
const outputValues = [];