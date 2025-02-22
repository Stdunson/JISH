function showSignInForm() {
    // Hide logo container
    document.getElementById('logoContainer').style.display = 'none';

    // Create sign-in form
    const signInForm = `
        <form id="signInForm" action="/signin" method="post">
            <input type="text" id="username" name="username" placeholder="Username" required>
            <input type="password" id="password" name="password" placeholder="Password" required>
            <div class="button-container">
                <button type="submit">Sign In</button>
                <button type="button" onclick="hideSignInForm()">Back</button>
            </div>
        </form>
    `;

    document.getElementById('signInFormContainer').innerHTML = signInForm;
    document.getElementById('signInFormContainer').style.display = 'block';
    document.getElementById('buttonContainer').style.display = 'none';
}

function hideSignInForm() {
    document.getElementById('logoContainer').style.display = 'block';
    document.getElementById('signInFormContainer').style.display = 'none';
    document.getElementById('buttonContainer').style.display = 'block';
}