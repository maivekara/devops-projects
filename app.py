from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    rastgele_sayi = random.randint(1, 100)
    return f"<h1>Rastgele Sayı: {rastgele_sayi}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
