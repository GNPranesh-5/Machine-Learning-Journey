import pandas as pd  
import pickle 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

df=pd.read_csv("../data/spam.csv")

x=df["message"]
y=df["label"]

vectorizer=CountVectorizer()
xvectorized=vectorizer.fit_transform(x)
model=LogisticRegression()
model.fit(xvectorized,y)

with open("../models/spammodel.pkl","wb") as file:
    pickle.dump(model,file)
with open("../models/vectorizer.pkl","wb") as file:
    pickle.dump(vectorizer,file)

print("Spam model saved successfully")