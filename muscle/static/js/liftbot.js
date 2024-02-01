function sendMessage() {
    
    const userInput = document.getElementById('user-input')
    const message = userInput.value.trim();

    if (message){

        // display and clear message
        displayMessage(message, 'user');
        userInput.value = '';

        const spinner = createSpinner();
        const chatArea = document.getElementById('chat-area');
        chatArea.appendChild(spinner);

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
        .catch(error => {
            console.error('Error:', error);
            spinner.style.display = 'none';
        });

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

function createSpinner() {
    const spinnerDiv = document.createElement('div');
    spinnerDiv.id = 'spinner';
    const spinnerImg = document.createElement('img');
    spinnerImg.src = spinnerURL;
    spinnerImg.alt = 'Loading...';

    spinnerImg.className = 'spinner-image';
    spinnerDiv.appendChild(spinnerImg);
    return spinnerDiv;
}