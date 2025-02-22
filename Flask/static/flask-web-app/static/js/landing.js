function showSignInForm() {
    // Hide the logo container
    document.getElementById('logoContainer').style.display = 'none';

    // Create the sign-in form
    const signInForm = `
        <form id="signInForm" action="/submit" method="post">
            <input type="text" id="username" name="username" placeholder="Username" required>
            <input type="password" id="password" name="password" placeholder="Password" required>
            <div class="button-container">
                <button type="submit">Sign In</button>
                <button type="button" onclick="hideSignInForm()">Back</button>
            </div>
        </form>
    `;

    // Insert the sign-in form into the container
    document.getElementById('signInFormContainer').innerHTML = signInForm;
    document.getElementById('signInFormContainer').style.display = 'block';

    // Hide the sign-in button
    document.getElementById('buttonContainer').style.display = 'none';
}

function hideSignInForm() {
    // Show the logo container
    document.getElementById('logoContainer').style.display = 'block';

    // Hide the sign-in form container
    document.getElementById('signInFormContainer').style.display = 'none';

    // Show the sign-in button
    document.getElementById('buttonContainer').style.display = 'block';
}