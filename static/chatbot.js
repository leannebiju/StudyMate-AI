// Function to handle the AI response
function askAI() {
    let userQuestion = document.getElementById("chatInput").value;
    let responseField = document.getElementById("chatResponse");

    // Check if the input is empty
    if (!userQuestion.trim()) {
        responseField.innerText = "Please enter a question.";
        return;
    }

    // Show a loading message while waiting for the response
    responseField.innerText = "Thinking...";

    // Make the API call to the backend
    fetch("/solve_doubt", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: userQuestion })
    })
    .then(response => response.json())
    .then(data => {
        // Display the AI's answer, or an error message if there's no answer
        responseField.innerText = data.answer || "AI could not generate an answer.";
    })
    .catch(error => {
        // In case of an error, display an error message
        responseField.innerText = "Error communicating with AI.";
        console.error(error);
    });
}

// Allow pressing the Enter key to trigger the askAI function
document.getElementById("chatInput").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        askAI();
    }
});