document.getElementById("editForm").addEventListener("submit", function (e) {
    // Prevent the default form submission behavior
    e.preventDefault();
  
    // Perform your validation checks
    if (!validatePassword()) {
      // If validation fails, show an error message and stop the function
      showCustomAlert("Passwords do not match.");
      return;
    }

    if (samePasswordAsBefore()){

        showCustomAlert("New password cannot be the same as old password.")
        return;
    }
  
    // If validation passes, proceed with form submission (e.g., using AJAX or a regular form submission)
    this.submit();
  });
  
  function validatePassword() {
    var password = document.getElementById("new").value;
    var confirmPassword = document.getElementById("new2").value;
    return password === confirmPassword;
  } // validatePassword()

  function samePasswordAsBefore(){
    var password = document.getElementById("password").value;
    var newPassword = document.getElementById("new").value;

    return password = newPassword;

  } //samePasswordAsBefore()
  
  function showCustomAlert(message) {
    document.getElementById("alertMessage").innerText = message;
    var alertModal = new bootstrap.Modal(
      document.getElementById("customAlertModal")
    );
    alertModal.show();
  }
  