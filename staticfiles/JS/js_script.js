
function validateForm() {
    var inputValue1 = document.getElementById("val1").value.trim();
    var inputValue2 = document.getElementById("val2").value.trim();
    


 if (isNaN(inputValue1) || isNaN(inputValue2)) {
        messageElement.textContent = "Input is not NUMER";
        return false; // Exit the function if inputs are empty
    } else if   (!inputValue1 || !inputValue2 ){
        messageElement.textContent = "Input is empty";
        return false;
    }

    num1 = Number(inputValue1);
    num2 = Number(inputValue2);
    out = num1 + num2;

    document.getElementById("result").textContent = "Total : " + out;
    messageElement.textContent = ""; // Clear any previous message
    return true;

}

document.getElementById("form_id").onsubmit = function() {
    return validateForm();
};


