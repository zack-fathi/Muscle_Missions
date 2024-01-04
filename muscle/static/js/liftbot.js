function sendMessage() {
    
    const userInput = document.getElementById('user-input')
    const message = userInput.value.trim();

    if (message){

        // display and clear message
        displayMessage(message, 'user');
        userInput.value = '';

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
