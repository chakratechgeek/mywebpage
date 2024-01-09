function validateForm() {
    var nameValue = document.getElementById("name").value.trim();
    var emailValue = document.getElementById("email").value.trim();
    var messageValue = document.getElementById('message').value.trim();
    var messageElement = document.getElementById('error-message'); // Define messageElement

    // Reset previous error message
    messageElement.textContent = "";


    // Check if last character of email is empty
    if (emailValue.slice(-1) === '') {
        messageElement.textContent = "Last character of email is empty";
        return false;
    }

    // Email validation using regular expression
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(emailValue)) {
        messageElement.textContent = "Invalid email format";
        return false;
    }

    // Rest of your validation logic...

    // If all validations pass, do other processing or submit the form
    return true;
}

window.onload = function() {
    var form = document.getElementById("form_id");
    form.onsubmit = function(event) {
        event.preventDefault(); // Prevent the default form submission behavior
        if (validateForm ()) {
            this.submit();
        }

    };
}