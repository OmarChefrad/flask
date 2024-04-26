from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data for todos
todos = {}

# GET all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(list(todos.values()))

# GET a single todo by ID
@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = todos.get(todo_id)
    if todo:
        return jsonify(todo)
    else:
        return jsonify({'message': 'Todo not found'}), 404

# POST a new todo
@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    if 'task' in data:
        todo_id = len(todos) + 1
        todos[todo_id] = {'id': todo_id, 'task': data['task'], 'completed': False}
        return jsonify(todos[todo_id]), 201
    else:
        return jsonify({'message': 'Task is required'}), 400

# PUT (update) a todo by ID
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = todos.get(todo_id)
    if todo:
        data = request.get_json()
        todo.update(data)
        return jsonify(todo)
    else:
        return jsonify({'message': 'Todo not found'}), 404

# DELETE a todo by ID
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = todos.pop(todo_id, None)
    if todo:
        return jsonify({'message': 'Todo deleted'})
    else:
        return jsonify({'message': 'Todo not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
