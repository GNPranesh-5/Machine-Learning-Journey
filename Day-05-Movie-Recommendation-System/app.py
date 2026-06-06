from flask import Flask,render_template,request
import pandas as pd  
app=Flask(__name__)

df=pd.read_csv("data/movies.csv")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend",methods=["POST"])
def recommend():
    movie=request.form["movie"]
    result=df[df["Movie"].str.lower()==movie.lower()]
    if result.empty:
        recommendations=["Movie not found"]
    else:
        genre=result.iloc[0]["Genre"]
        recommendations=df[(df["Genre"]==genre)&(df["Movie"]!=result.iloc[0]["Movie"])]["Movie"].tolist()
        
    return render_template("index.html",recommendations=recommendations)
if __name__=="__main__":
    app.run(debug=True)