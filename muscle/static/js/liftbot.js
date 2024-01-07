function sendMessage() {
    
    const userInput = document.getElementById('user-input')
    const message = userInput.value.trim();
    const spinner = document.getElementById("#spinner");
    console.log(spinner.style.display);

    if (message){

        spinner.style.display = 'block';
        console.log(spinner.style.display);

        // display and clear message
        displayMessage(message, 'user');
        userInput.value = '';

        fetch('/process_message/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message }),
            
        })
        .then(response => response.json())
        .then(data => {
            displayMessage(data.response, 'bot');
            spinner.style.display = 'none';

        })
        .catch(error => console.error('Error:', error));
        spinner.style.display = 'none';

    }



}

function displayMessage(text, sender){

    // append the message to chat area
    const chatWindow = document.getElementById('chat-area');
    const messageDiv = document.createElement('div');
    messageDiv.className = sender + '-message message';
    messageDiv.textContent = text;
    chatWindow.appendChild(messageDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight;

}

document.getElementById('send-btn').addEventListener('click', sendMessage);

document.getElementById('user-input').addEventListener('keypress', function(event) {
    if (event.keyCode === 13) { 
        sendMessage();
        event.preventDefault();
    }
});
