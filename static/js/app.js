import { createMessage } from './messageUtils.js';

const form = document.getElementById('input-form');
const input = document.getElementById('user-input');
const messages = document.getElementById('messages');
const welcomeScreen = document.getElementById('welcome-screen');
const sendButton = document.getElementById('send-button');

form.addEventListener('submit', async (e) => {
    e.preventDefault(); // Prevent the page from refreshing when the form is submitted
    
    const content = input.value.trim();
    if (!content) return;

    // Hide welcome screen if visible
    if (welcomeScreen.style.display !== 'none') {
        welcomeScreen.style.display = 'none';
    }

    // Add user message
    createMessage(content, 'user');
    input.value = '';
    sendButton.disabled = true;  // Disable the button

    // Show loading state
    const loadingDiv = document.createElement('div');
    loadingDiv.className = 'loading';
    loadingDiv.innerHTML = `
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M21 12a9 9 0 1 1-6.219-8.56"/>
        </svg>
        Analyzing content...
    `;
    messages.appendChild(loadingDiv);

    try {
        // Get analysis from the Flask backend
        const response = await fetch('/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ content })
        });

        const data = await response.json();

        // Remove loading state and add the response message
        loadingDiv.remove();
        createMessage(data.analysis, 'assistant');

        // Re-enable the button
        sendButton.disabled = false;  // Enable the button again after response

    } catch (error) {
        console.error("Error:", error);
        loadingDiv.remove();
        createMessage("Sorry, something went wrong. Please try again.", 'assistant');
        
        // Re-enable the button in case of error
        sendButton.disabled = false;
    }
});

// Enable/disable send button based on input
input.addEventListener('input', () => {
    sendButton.disabled = !input.value.trim();  // Enable/disable button based on input
});
