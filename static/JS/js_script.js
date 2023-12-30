
function add() {
    console.log("Chakra");
    var num1, num2, out, inputValue1, inputValue2, messageElement;

    inputValue1 = document.getElementById("val1").value.trim();
    inputValue2 = document.getElementById("val2").value.trim();
    messageElement = document.getElementById('message');

    if (isNaN(inputValue1) || isNaN(inputValue2)) {
        messageElement.textContent = "Input is not NUMER";
        return; // Exit the function if inputs are empty
    } else if   (!inputValue1 || !inputValue2 ){
        messageElement.textContent = "Input is empty";
        return;
    }

    num1 = Number(inputValue1);
    num2 = Number(inputValue2);
    out = num1 + num2;

    document.getElementById("result").textContent = "Total : " + out;
    messageElement.textContent = ""; // Clear any previous message
}

function clr() {
    document.getElementById("val1").value = "";
    document.getElementById("val2").value = "";
    document.getElementById("result").innerHTML = "";
    document.getElementById('message').textContent = ""; // Clear any previous message
}
