from flask import Flask, render_template, request

app = Flask(__name__)

# Define the quiz questions
questions = [
    {"question": "What is the capital of France?", "options": ["London", "Berlin", "Paris", "Rome"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
    {"question": "What is the largest mammal?", "options": ["Elephant", "Blue Whale", "Giraffe", "Shark"], "answer": "Blue Whale"},
    {"question": "Which language is primarily used for web development?", "options": ["Python", "JavaScript", "C++", "Swift"], "answer": "JavaScript"},
    {"question": "What is the chemical symbol for water?", "options": ["CO2", "O2", "H2O", "N2"], "answer": "H2O"},
    {"question": "What is the currency of Japan?", "options": ["Yen", "Dollar", "Euro", "Pound"], "answer": "Yen"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["Shakespeare", "Hemingway", "Tolstoy", "Dickens"], "answer": "Shakespeare"},
    {"question": "Which ocean is the largest?", "options": ["Atlantic", "Indian", "Pacific", "Arctic"], "answer": "Pacific"},
    {"question": "What gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
    {"question": "Who was the first person to walk on the moon?", "options": ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "Michael Collins"], "answer": "Neil Armstrong"}
]

@app.route('/')
def quiz():
    return render_template("quiz.html", questions=questions, enumerate=enumerate)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for index, question in enumerate(questions):
        selected_option = request.form.get(f"question-{index}")
        if selected_option == question["answer"]:
            score += 1
    return render_template("result.html", score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)