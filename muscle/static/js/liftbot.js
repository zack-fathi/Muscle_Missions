function sendMessage() {
    
    const userInput = document.getElementById('user-input')
    const message = userInput.value.trim();
    console.log("Hello")

    if (message){

        // display and clear message
        console.log(message)
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

        })
        .catch(error => console.error('Error:', error));

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
