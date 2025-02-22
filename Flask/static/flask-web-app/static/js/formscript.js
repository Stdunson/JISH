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

function toggleUnknown(inputId) {
    const inputField = document.getElementById(inputId);
    const unknownCheckbox = document.getElementById(inputId + 'Unknown');
    if (unknownCheckbox.checked) {
        inputField.disabled = true;
        inputField.value = '-1';
    } else {
        inputField.disabled = false;
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
    const idkSteps = [6, 7, 8, 9, 10, 11, 12];

    if(moneySteps.includes(step)){
        if(document.getElementById(`step${step}`).querySelector('input').value === ''){
            return false;
        }
        if(!idkSteps.includes(step)){
            if(document.getElementById(`step${step}`).querySelector('input').value < 0){
                return false;
            }
        }
    }

    if(boxSteps.includes(step)){
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

    if(idkSteps.includes(step)){
        const input = document.getElementById(`step${step}`).querySelector('input[type="number"]');
        const checkbox = document.getElementById(`step${step}`).querySelector('input[type="checkbox"]');
        if(input && checkbox && !checkbox.checked){
            if(input.value === ''){
                return false;
            }
            if(input.value < 0){
                return false;
            }
        }
    }

    return true;
}