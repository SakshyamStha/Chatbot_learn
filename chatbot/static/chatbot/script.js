document.getElementById('send-button').onclick = function() {
    const userInput = document.getElementById('user-input');
    const userMessage = userInput.value;

    // Add user message to chat box
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<div class="user-message">You:${userMessage}</div>`;
    userInput.value = ''; // Clear input

    // Send user message to chatbot
    fetch(`/chatbot/?message=${encodeURIComponent(userMessage)}`)
        .then(response => response.json())
        .then(data => {
            chatBox.innerHTML += `<div class="bot-message">Bot:${data.response}</div>`;
            chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
        });
};
