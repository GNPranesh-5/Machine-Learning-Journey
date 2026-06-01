from flask import Flask,render_template,request
import pickle
import pandas as pd  
app=Flask(__name__)

with open("models/HouseModel.pkl","rb") as file:
    model=pickle.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    size=float(request.form["size"])
    bedrooms=int(request.form["bedrooms"])
    data=pd.DataFrame({
      "Size":[size],
      "Bedrooms":[bedrooms]  
    })

    prediction=model.predict(data)[0]

    return render_template(
        "index.html",
        prediction=round(prediction,2)
    )
if __name__ == "__main__":
    app.run(debug=True)