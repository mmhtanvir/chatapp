const socket = io();

let messageContainer = document.querySelector(".flex-grow-1.p-3.overflow-auto");

socket.on("connect", () => {
    let p = document.createElement("p");
    p.innerText = "You're connected";
    messageContainer.appendChild(p);
});

let messageInput = document.getElementById("msg");
messageInput.addEventListener("keypress", (e) => {
    if (e.which === 13) {
        socket.emit("message", messageInput.value);
        messageInput.value = "";
    }
});

socket.on('message', (message) => {
    let messageElement = document.createElement("p");
    messageContent.innerText = message;
    messageElement.appendChild(messageContent);
});


socket.on('message', (message) => {
    let messageElement = document.createElement("p")
    messageElement.innerText = message
    messageContainer.appendChild(messageElement)
})