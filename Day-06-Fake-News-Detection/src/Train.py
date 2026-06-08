import pandas as pd  
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

df=pd.read_csv("../data/news.csv")
x=df["text"]
y=df["label"]
vectorizer=CountVectorizer()
xvector=vectorizer.fit_transform(x)
model=LogisticRegression()
model.fit(xvector,y)
with open("../models/fakenewsmodel.pkl","wb") as file:
    pickle.dump(model,file)
with open("../models/vectorizer.pkl","wb") as file:
    pickle.dump(vectorizer,file)

print("Fake news model saved successfully")