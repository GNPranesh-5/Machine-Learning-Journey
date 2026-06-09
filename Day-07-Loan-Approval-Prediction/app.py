from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

with open("models/loanmodel.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    income = float(request.form["income"])
    creditscore = float(request.form["credit_score"])
    loanamount = float(request.form["loan_amount"])

    data = pd.DataFrame({
        "Income": [income],
        "CreditScore": [creditscore],
        "LoanAmount": [loanamount]
    })

    prediction = model.predict(data)[0]

    result = "Loan Approved ✅" if prediction == 1 else "Loan Rejected ❌"

    return render_template(
        "index.html",
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)