document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements - Toggle Widget
    const toggleBtn = document.getElementById('chatbot-toggle-btn');
    const chatbotWindow = document.getElementById('chatbot-window');
    const closeChatBtn = document.getElementById('close-chat-btn');

    // DOM Elements - Onboarding
    const deptSelect = document.getElementById('department');
    const cutoffDisplay = document.getElementById('cutoff-display');
    const cutoffValue = document.getElementById('cutoff-value');
    const nameSection = document.getElementById('name-section');
    const userNameInput = document.getElementById('user-name');
    const startChatBtn = document.getElementById('start-chat-btn');
    const errorMsg = document.getElementById('onboarding-error');
    
    // DOM Elements - Sections
    const onboardingSection = document.getElementById('onboarding-section');
    const chatSection = document.getElementById('chat-section');
    
    // DOM Elements - Chat Interface
    const userInfoDisplay = document.getElementById('user-info-display');
    const restartBtn = document.getElementById('restart-btn');
    const chatMessages = document.getElementById('chat-messages');
    const chatInput = document.getElementById('chat-input');
    const sendBtn = document.getElementById('send-btn');
    const typingIndicator = document.getElementById('typing-indicator');

    let userName = '';
    let userDept = '';
    let isWaitingForResponse = false; // Prevent duplicate sends

    // --- Widget Toggle Logic ---
    toggleBtn.addEventListener('click', () => {
        chatbotWindow.classList.remove('hidden');
        toggleBtn.style.transform = 'scale(0)'; // hide button when open
        
        // Auto focus input if chat is active
        if (!chatSection.classList.contains('hidden')) {
            setTimeout(() => chatInput.focus(), 300);
        }
    });

    closeChatBtn.addEventListener('click', () => {
        chatbotWindow.classList.add('hidden');
        toggleBtn.style.transform = 'scale(1)'; // show button when closed
    });

    // --- Step 1: Department Selection ---
    deptSelect.addEventListener('change', function() {
        const selectedOption = this.options[this.selectedIndex];
        const cutoff = selectedOption.getAttribute('data-cutoff');
        
        if (cutoff) {
            cutoffValue.textContent = cutoff;
            cutoffDisplay.classList.remove('hidden');
            nameSection.classList.remove('hidden');
            errorMsg.textContent = '';
            userDept = this.value;
            // Scroll down a bit to show name input
            onboardingSection.scrollTop = onboardingSection.scrollHeight;
        }
    });

    // --- Step 2: Start Chat ---
    startChatBtn.addEventListener('click', startChatSession);
    userNameInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            startChatSession();
        }
    });

    function startChatSession() {
        userName = userNameInput.value.trim();
        
        if (!userDept) {
            errorMsg.textContent = "Please select a department.";
            return;
        }
        if (!userName) {
            errorMsg.textContent = "Please enter your name.";
            return;
        }
        
        // Disable button during load
        startChatBtn.disabled = true;
        startChatBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
        
        // Send data to backend to set session
        fetch('/start', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name: userName, department: userDept })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                errorMsg.textContent = data.error;
                startChatBtn.disabled = false;
                startChatBtn.textContent = 'Start Chat';
            } else {
                // Success, transition to chat
                transitionToChat(data.welcome_msg);
            }
        })
        .catch(error => {
            errorMsg.textContent = "An error occurred connecting to server.";
            startChatBtn.disabled = false;
            startChatBtn.textContent = 'Start Chat';
            console.error('Error:', error);
        });
    }

    function transitionToChat(welcomeMsg) {
        onboardingSection.classList.add('hidden');
        chatSection.classList.remove('hidden');
        
        // Display short name in header
        userInfoDisplay.textContent = userName.split(' ')[0] + ' | ' + userDept;
        
        // Add welcome message from bot
        addMessage(welcomeMsg, 'bot');
        
        // Focus input
        setTimeout(() => chatInput.focus(), 300);
    }

    // --- Step 3: Chat Interaction ---
    sendBtn.addEventListener('click', sendMessage);
    chatInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    function sendMessage() {
        const text = chatInput.value.trim();
        
        // Prevent sending if empty or waiting for bot response
        if (!text || isWaitingForResponse) return;

        // Add user message to UI
        addMessage(text, 'user');
        
        // Clear input and block new messages
        chatInput.value = '';
        setChatState(false); 
        
        // Show typing indicator
        showTyping(true);

        // Send to backend
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: text })
        })
        .then(response => response.json())
        .then(data => {
            showTyping(false);
            if (data.error) {
                addMessage(data.error, 'bot');
            } else {
                addMessage(data.response, 'bot');
            }
            setChatState(true);
        })
        .catch(error => {
            showTyping(false);
            addMessage("Sorry, I'm having trouble connecting to the server.", 'bot');
            setChatState(true);
            console.error('Error:', error);
        });
    }
    
    function setChatState(enabled) {
        isWaitingForResponse = !enabled;
        chatInput.disabled = !enabled;
        sendBtn.disabled = !enabled;
        if (enabled) {
            chatInput.focus();
        }
    }

    function addMessage(text, sender) {
        const msgDiv = document.createElement('div');
        msgDiv.classList.add('message');
        msgDiv.classList.add(sender === 'user' ? 'user-msg' : 'bot-msg');
        msgDiv.textContent = text;
        
        // Insert message BEFORE the typing indicator
        chatMessages.insertBefore(msgDiv, typingIndicator);
        scrollToBottom();
    }

    function showTyping(show) {
        if (show) {
            typingIndicator.classList.remove('hidden');
        } else {
            typingIndicator.classList.add('hidden');
        }
        scrollToBottom();
    }

    function scrollToBottom() {
        // Use a slight timeout to ensure DOM has updated before scrolling
        setTimeout(() => {
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }, 10);
    }

    // --- Restart Flow ---
    restartBtn.addEventListener('click', () => {
        if(confirm("Are you sure you want to end this chat and start over?")) {
            location.reload();
        }
    });
});
