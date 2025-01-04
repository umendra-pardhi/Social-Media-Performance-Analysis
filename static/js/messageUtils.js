import { marked } from "https://cdn.jsdelivr.net/npm/marked/lib/marked.esm.js";
// Select the messages container globally
const messages = document.getElementById('messages');

// Function to create a new message and append it to the chat container
export function createMessage(content, type) {
    // Create a div element for the message container
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type}`;  // 'user' or 'assistant'

    // Create another div for the message content
    const messageContent = document.createElement('div');
    messageContent.className = 'message-content';
    messageContent.innerHTML =  marked.parse(content);  // Set the message content (user input or assistant response)
    
    // Append message content to message div
    messageDiv.appendChild(messageContent);
    
    // Append the message div to the messages container
    messages.appendChild(messageDiv);
    
    // Ensure the chat window scrolls to the bottom after each message
    messages.scrollTop = messages.scrollHeight;
}


