<!DOCTYPE html>
<html>
    <head>
        <title>To-Do List</title>
        <style>
            /* Add some basic styling */
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
            }
            h1 {
                text-align: center;
            }
            ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
            }
            li {
                margin: 10px 0;
                padding: 10px;
                background-color: #f2f2f2;
                border-radius: 5px;
            }
            li.checked {
                background-color: #ccc;
                text-decoration: line-through;
            }
            input[type="text"] {
                width: 100%;
                padding: 12px 20px;
                margin: 10px 0;
                box-sizing: border-box;
                border: none;
                border-radius: 5px;
            }
            button {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 12px 20px;
                margin: 10px 0;
                cursor: pointer;
            }
            button:hover {
                background-color: #3e8e41;
            }
        </style>
    </head>
    <body>
        <h1>To-Do List</h1>
        <input type="text" id="taskInput" placeholder="Add new task...">
        <button onclick="addTask()">Add</button>
        <ul id="taskList">
        </ul>
        <script>
            function addTask() {
                var input = document.getElementById("taskInput");
                var ul = document.getElementById("taskList");
                var li = document.createElement("li");
                li.appendChild(document.createTextNode(input.value));
                ul.appendChild(li);
                input.value = "";
                li.onclick = function() {
                    this.classList.toggle("checked");
                }
            }
        </script>
    </body>
</html>
