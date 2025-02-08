document.addEventListener("DOMContentLoaded", function () {
    let workTime = 25 * 60;
    let breakTime = 5 * 60;
    let timeLeft = workTime;
    let isBreak = false;
    let timerInterval = null;

    const timeDisplay = document.getElementById("time-display");
    const startBtn = document.getElementById("start-btn");
    const resetBtn = document.getElementById("reset-btn");
    const message = document.getElementById("timer-message");
    const restartBtn = document.getElementById("restart-btn");
    const cancelBtn = document.getElementById("cancel-btn");
    const buttonContainer = document.getElementById("button-container");

    function updateDisplay() {
        let minutes = Math.floor(timeLeft / 60);
        let seconds = timeLeft % 60;
        timeDisplay.textContent = `${minutes}:${seconds < 10 ? "0" : ""}${seconds}`;
    }

    function startTimer() {
        if (timerInterval === null) {
            timerInterval = setInterval(() => {
                if (timeLeft > 0) {
                    timeLeft--;
                    updateDisplay();
                } else {
                    clearInterval(timerInterval);
                    timerInterval = null;

                    if (!isBreak) {
                        isBreak = true;
                        timeLeft = breakTime;
                        message.textContent = "Break Time! Relax for 5 minutes.";
                    } else {
                        message.textContent = "Pomodoro Session Complete!";
                        buttonContainer.style.display = "block";
                        return;
                    }

                    updateDisplay();
                    startTimer();
                }
            }, 1000);
        }
    }

    function resetTimer() {
        clearInterval(timerInterval);
        timerInterval = null;
        isBreak = false;
        timeLeft = workTime;
        updateDisplay();
        message.textContent = "Start your Pomodoro session!";
        buttonContainer.style.display = "none";
    }

    function restartSession() {
        resetTimer();
        startTimer();
    }

    function cancelSession() {
        resetTimer();
        message.textContent = "Session canceled. Start a new one anytime.";
    }

    startBtn.addEventListener("click", startTimer);
    resetBtn.addEventListener("click", resetTimer);
    restartBtn.addEventListener("click", restartSession);
    cancelBtn.addEventListener("click", cancelSession);

    updateDisplay();
});
