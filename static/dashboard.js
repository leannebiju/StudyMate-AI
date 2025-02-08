document.addEventListener("DOMContentLoaded", function () {
    const noteForm = document.getElementById("noteForm");
    const noteInput = document.getElementById("noteInput");

    noteForm.addEventListener("submit", function (e) {
        if (!noteInput.value.trim()) {
            e.preventDefault();
            alert("Please enter a note.");
        }
    });
});
