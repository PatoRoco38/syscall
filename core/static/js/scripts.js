//Faz sumir a mensagem de erro na tela de login ao começar a digitar o email
document.addEventListener("DOMContentLoaded", function() {
    const emailInput = document.getElementById("typeEmailX");
    if (emailInput) {
        emailInput.addEventListener("input", function() {
            const alertDiv = document.querySelector(".alert.alert-danger");
            if (alertDiv) {
                alertDiv.style.display = "none";
            }
        });
    }
});