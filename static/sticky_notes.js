function addStickyNote() {
    let noteText = document.getElementById("noteInput").value.trim();
    if (!noteText) {
        alert("Note cannot be empty!");
        return;
    }

    fetch("/add_note", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ note: noteText })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            let notesContainer = document.getElementById("notesContainer");
            let noteDiv = document.createElement("div");
            noteDiv.classList.add("sticky-note");
            noteDiv.id = `note-${data.id}`;
            noteDiv.innerHTML = `<p>${data.note}</p> 
                                 <button class="btn btn-danger btn-sm" onclick="deleteNote(${data.id})">X</button>`;
            notesContainer.appendChild(noteDiv);
            document.getElementById("noteInput").value = "";
        }
    })
    .catch(error => console.error("Error:", error));
}

function deleteNote(noteId) {
    fetch(`/delete_note/${noteId}`, { method: "DELETE" })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.getElementById(`note-${noteId}`).remove();
        } else {
            alert("Failed to delete note.");
        }
    })
    .catch(error => console.error("Error:", error));
}
