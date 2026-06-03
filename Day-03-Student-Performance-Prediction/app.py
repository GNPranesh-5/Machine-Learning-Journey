from flask import Flask, render_template, request
import pickle
import pandas as pd  

app=Flask(__name__)

with open("models/studentmodel.pkl","rb") as file:
    model=pickle.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    studyhours=float(request.form["StudyHours"])
    attendance=float(request.form["Attendance"])
    assignments=int(request.form["Assignments"])

    data=pd.DataFrame({
        "StudyHours":[studyhours],
        "Attendance":[attendance],
        "Assignments":[assignments]
    })

    prediction=model.predict(data)[0]

    return render_template("index.html",prediction=round(prediction,2))

if __name__ == "__main__":
    app.run(debug=True)
