from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open("models/fakenewsmodel.pkl", "rb") as file:
    model = pickle.load(file)

with open("models/vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    news = request.form["news"]

    news_vector = vectorizer.transform([news])

    prediction = model.predict(news_vector)[0]

    return render_template(
        "index.html",
        prediction=prediction,
        news=news
    )

if __name__ == "__main__":
    app.run(debug=True)