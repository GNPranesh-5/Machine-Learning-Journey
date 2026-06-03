from flask import Flask, render_template, request
import pickle

app=Flask(__name__)

with open("models/spammodel.pkl","rb") as file:
    model=pickle.load(file)
with open("models/vectorizer.pkl","rb") as file:
    vectorizer=pickle.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    message=request.form["message"]
    msgvector=vectorizer.transform([message])
    prediction=model.predict(msgvector)[0]
    return render_template("index.html",prediction=prediction,message=message)

if __name__ == "__main__":
    app.run(debug=True)