from flask import Flask, render_template, request

app = Flask(__name__)

# Mock data for questions and answers
questions = [
    {
        'id': 1,
        'question': 'What is a SQL injection attack?'
    },
    {
        'id': 2,
        'question': 'What is XSS (Cross-Site Scripting)?'
    }
]

answers = {
    1: ['Injecting malicious SQL code into an application'],
    2: ['Injecting malicious scripts into web pages viewed by other users']
}

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    user_answers = {int(key): value for key, value in request.form.items()}
    score = 0
    for question_id, answer in user_answers.items():
        if answer in answers.get(question_id, []):
            score += 1
    return f'Your score: {score}/{len(questions)}'

if __name__ == '__main__':
    app.run(debug=True)
