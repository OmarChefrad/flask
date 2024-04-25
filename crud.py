from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data for todos
todos = [
    {"id": 1, "task": "Buy groceries", "completed": False},
    {"id": 2, "task": "Walk the dog", "completed": True},
    {"id": 3, "task": "Do laundry", "completed": False}
]

# GET all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# GET a single todo by ID
@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    if todo:
        return jsonify(todo)
    else:
        return jsonify({'message': 'Todo not found'}), 404

# POST a new todo
@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    if 'task' in data:
        new_todo = {'id': len(todos) + 1, 'task': data['task'], 'completed': False}
        todos.append(new_todo)
        return jsonify(new_todo), 201
    else:
        return jsonify({'message': 'Task is required'}), 400

# PUT (update) a todo by ID
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    if todo:
        data = request.get_json()
        todo.update(data)
        return jsonify(todo)
    else:
        return jsonify({'message': 'Todo not found'}), 404

# DELETE a todo by ID
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return jsonify({'message': 'Todo deleted'})

if __name__ == '__main__':
    app.run(debug=True)
