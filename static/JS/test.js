function validateForm() {
    var inputValue1 = document.getElementById("val1").value.trim();
    var inputValue2 = document.getElementById("val2").value.trim();
    var messageElement = document.getElementById('message'); // Define messageElement

    if (isNaN(inputValue1) || isNaN(inputValue2)) {
        messageElement.textContent = "Input is not a number";
        return false; // Exit the function if inputs are not numbers
    } else if (!inputValue1 || !inputValue2) {
        messageElement.textContent = "Input is empty";
        return false;
    }

    var num1 = Number(inputValue1);
    var num2 = Number(inputValue2);
    var out = num1 + num2;

    document.getElementById("result").textContent = "Total : " + out;
    messageElement.textContent = ""; // Clear any previous message
    return true;
}

function clearForm() {
    document.getElementById("val1").value = ""; // Clear value of input field val1
    document.getElementById("val2").value = ""; // Clear value of input field val2
    document.getElementById("message").textContent = ""; // Clear any displayed message
    document.getElementById("result").textContent = "-"; // Reset the result display
}

window.onload = function() {
    var form = document.getElementById("form_id");
    form.onsubmit = function(event) {
        event.preventDefault(); // Prevent the default form submission behavior
        validateForm(); // Call the validateForm function
    };

    var clearButton = document.getElementById("clear");
    if (clearButton) {
        clearButton.addEventListener("click", function(event) {
            event.preventDefault(); // Prevent default button behavior (form submission)
            clearForm(); // Call the clearForm function
        });
    }
};

