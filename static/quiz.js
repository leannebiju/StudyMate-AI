async function generateQuiz() {
    let topic = document.getElementById("quizTopic").value.trim();
    let difficulty = document.getElementById("quizDifficulty").value;
    let numQuestions = document.getElementById("quizNumQuestions").value;
    let quizContainer = document.getElementById("quizContainer");

    quizContainer.innerHTML = "<p>Loading quiz...</p>";

    try {
        let response = await fetch("/generate_quiz", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ topic, difficulty, num_questions: numQuestions }),
        });

        let data = await response.json();

        if (response.ok) {
            displayQuiz(data.quiz);
        } else {
            quizContainer.innerHTML = `<p style="color: red;">Error: ${data.error}</p>`;
        }
    } catch (error) {
        quizContainer.innerHTML = `<p style="color: red;">Request Failed. Check console for errors.</p>`;
        console.error("Quiz API Error:", error);
    }
}




function displayQuiz(quizQuestions) {
    let quizContainer = document.getElementById("quizContainer");
    quizContainer.innerHTML = "";

    quizQuestions.forEach((q, index) => {
        let questionId = `answer-${index}`; // Unique ID for each answer section

        let questionHTML = `<div class="question">
            <p><strong>Q${index + 1}:</strong> ${q.question}</p>
            <ul>
                <li>A) ${q.options.A}</li>
                <li>B) ${q.options.B}</li>
                <li>C) ${q.options.C}</li>
                <li>D) ${q.options.D}</li>
            </ul>
            <button onclick="showAnswer('${questionId}')">Show Answer</button>
            <p id="${questionId}" style="display: none;"><strong>Correct Answer:</strong> ${q.correct_answer}</p>
        </div>`;

        quizContainer.innerHTML += questionHTML;
    });
}

// Function to reveal the correct answer when the button is clicked
function showAnswer(answerId) {
    let answerElement = document.getElementById(answerId);
    if (answerElement.style.display === "none") {
        answerElement.style.display = "block";
    } else {
        answerElement.style.display = "none";
    }
}


