function askAI() {
    let userQuestion = document.getElementById("chatInput").value;
    let responseField = document.getElementById("chatResponse");

    if (!userQuestion) {
        responseField.innerText = "Please enter a question.";
        return;
    }

    fetch("/solve_doubt", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: userQuestion })
    })
    .then(response => response.json())
    .then(data => {
        responseField.innerText = data.answer || "AI could not generate an answer.";
    })
    .catch(error => {
        responseField.innerText = "Error communicating with AI.";
        console.error(error);
    });
}
