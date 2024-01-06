document.getElementById("signupForm").addEventListener("submit", function (e) {
  // Prevent the default form submission behavior
  e.preventDefault();

  // Perform your validation checks
  if (!validatePassword()) {
    // If validation fails, show an error message and stop the function
    showCustomAlert("Passwords do not match.");
    return;
  }

  // If validation passes, proceed with form submission (e.g., using AJAX or a regular form submission)
  this.submit();
});

function validatePassword() {
  var password = document.getElementById("password").value;
  var confirmPassword = document.getElementById("confirm-password").value;
  return password === confirmPassword;
} // validatePassword()

function showCustomAlert(message) {
  document.getElementById("alertMessage").innerText = message;
  var alertModal = new bootstrap.Modal(
    document.getElementById("customAlertModal")
  );
  alertModal.show();
}
