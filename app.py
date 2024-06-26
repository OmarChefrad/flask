from flask import Flask, jsonify
import concurrent.futures
import time

app = Flask(__name__)

def time_consuming_task():
    # Simulate a time-consuming task
    time.sleep(5)
    return 'Task completed'

@app.route('/task1')
def endpoint1():
    # Execute the time-consuming task concurrently using threads
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(time_consuming_task)
        result = future.result()  # This blocks until the task is completed
    return jsonify({'result': result})
from flask import Flask, jsonify
import asyncio

app = Flask(__name__)

async def time_consuming_task():
    # Simulate a time-consuming task
    await asyncio.sleep(5)
    return 'Task completed'
    
@app.route('/sequential')
def sequential_endpoint():
    # Execute time-consuming task sequentially (blocking)
    result = time_consuming_task(5)
    return jsonify({'result': result})

@app.route('/task1')
async def endpoint1():
    # Execute the time-consuming task asynchronously
    result = await time_consuming_task()
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/task2')
def endpoint2():
    # Execute the time-consuming task concurrently using threads
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(time_consuming_task)
        result = future.result()  # This blocks until the task is completed
    return jsonify({'result': result})

@app.route('/task3')
def endpoint3():
    # Simulate a time-consuming task
    time.sleep(5)
    return jsonify({'result': 'Task completed'})

if __name__ == '__main__':
    app.run(debug=True)
