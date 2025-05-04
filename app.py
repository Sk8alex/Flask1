from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"
app.config['JSON_AS_ASCII'] = False

about_me = {
    "name": "Евгений",
    "surname": "Юрченко",
    "email": "eyurchenko@specialist.ru"
}

quotes = [
    {
        "id": 1,
        "author": "Rick Cook",
        "text": "Программирование сегодня — это гонка разработчиков программ, стремящихся писать программы с большей и лучшей идиотоустойчивостью, и вселенной, котораяпытается создать больше отборных идиотов. Пока вселенная побеждает."
    },
    {
        "id": 2,
        "author": "Waldi Ravens",
        "text": "Программирование на С похоже на быстрые танцы на только что отполированном полу людей с острыми бритвами в уках."
    },
    {
        "id": 3,
        "author": "Mosher’s Law of Software Engineering",
        "text": "Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили."
    },
    {
        "id": 4,
        "author": "Yoggi Berra",
        "text": "В теории, теория и практика неразделимы. Напрактике это не так."
    },
]

@app.get("/quotes")
def get_quotes():
    return jsonify(quotes)

@app.route('/quotes/<int:quote_id>', methods=['GET'])
def get_quote(quote_id):
    for quote in quotes:
        if quote['id'] == quote_id:
            return jsonify(quote)
    return f"Quote with id={id} not found", 404


@app.route('/quotes/count', methods=['GET'])
def get_quotes_count():
    count = len(quotes)
    return jsonify({"count": count})

@app.route('/quotes/random', methods=['GET'])
def get_random_quote():
    quote = random.choice(quotes)
    return jsonify(quote)

@app.route("/about")
def about():
    return about_me

if __name__ == "__main__":
    app.run(debug=True)