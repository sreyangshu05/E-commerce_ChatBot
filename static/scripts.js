// Wait for the DOM to load before running any scripts
document.addEventListener("DOMContentLoaded", () => {
    // References to key DOM elements
    const userInfo = document.getElementById("user-info");
    const chatBox = document.getElementById("chat-box");
    const resetButton = document.getElementById("reset-btn");
    const clearChatButton = document.getElementById("clear-chat");
    const userInputField = document.getElementById("user-input");

    // Fetch and display chat logs for the current user
    fetch("/chat-logs")
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                userInfo.textContent = "Please log in.";
            } else {
                userInfo.textContent = "Welcome back!";
                data.forEach(log => {
                    const message = document.createElement("div");
                    message.innerHTML = `<span>${log.timestamp}</span>: ${log.message}`;
                    chatBox.appendChild(message);
                });
            }
        });

    // Handle Enter key press in the user input field
    userInputField.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            const userInput = event.target.value.trim(); // Get and trim the user input
            if (userInput) {
                // Fetch search results based on user input
                fetch(`/search?query=${userInput}`)
                    .then(response => response.json())
                    .then(data => {
                        chatBox.innerHTML = ''; // Clear previous search results
                        
                        if (data.length > 0) {
                            data.forEach(product => {
                                // Create a message element to display product details
                                const message = document.createElement("div");
                                message.innerHTML = `<strong>${product[1]}</strong><br>Description: ${product[2]}<br>Price: ${product[3]}<br>Stock: ${product[4]}`;
                                chatBox.appendChild(message);
                            });
                        } else {
                            const message = document.createElement("div");
                            message.innerText = "No products found.";
                            chatBox.appendChild(message);
                        }
                    })
                    .catch(error => {
                        console.error("Error fetching products:", error);
                        const message = document.createElement("div");
                        message.innerText = "There was an error fetching the data. Please try again.";
                        chatBox.appendChild(message);
                    });
                event.target.value = ""; // Clear the input field
            }
        }
    });

    document.getElementById("clear-chat").addEventListener("click", function () {
        document.getElementById("chat-box").innerHTML = "";
    });
});
