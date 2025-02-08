document.addEventListener("DOMContentLoaded", function () {
    const todoForm = document.getElementById("todoForm");
    const todoInput = document.getElementById("todoInput");
    const todoTime = document.getElementById("todoTime");
    const todoList = document.getElementById("todoList");

    function loadTasks() {
        todoList.innerHTML = "";
        const tasks = JSON.parse(localStorage.getItem("tasks")) || [];
        tasks.forEach((task, index) => {
            addTaskToDOM(task.text, task.time, index);
        });
    }

    function saveTasks(tasks) {
        localStorage.setItem("tasks", JSON.stringify(tasks));
    }

    function addTaskToDOM(text, time, index) {
        const li = document.createElement("li");
        li.className = "list-group-item d-flex justify-content-between align-items-center";
        li.innerHTML = `<span>${text} - <strong>${time}</strong></span>
                        <button class="btn btn-danger btn-sm" onclick="deleteTask(${index})">Delete</button>`;
        todoList.appendChild(li);
    }

    todoForm.addEventListener("submit", function (e) {
        e.preventDefault();
        const text = todoInput.value.trim();
        const time = todoTime.value.trim();
        if (text && time) {
            let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
            tasks.push({ text, time });
            saveTasks(tasks);
            addTaskToDOM(text, time, tasks.length - 1);
            todoInput.value = "";
            todoTime.value = "";
        }
    });

    window.deleteTask = function (index) {
        let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
        tasks.splice(index, 1);
        saveTasks(tasks);
        loadTasks();
    };

    loadTasks();
});
