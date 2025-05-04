from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

about_me = {
    "name": "Евгений",
    "surname": "Юрченко",
    "email": "eyurchenko@specialist.ru"
}
@app.route("/about")
def about():
    return about_me

if __name__ == "__main__":
    app.run(debug=True)