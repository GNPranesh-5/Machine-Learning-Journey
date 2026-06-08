import pickle

with open("../models/fakenewsmodel.pkl","rb") as file:
    model=pickle.load(file)
with open("../models/vectorizer.pkl","rb") as file:
    vectorizer=pickle.load(file)

news=input("Enter news: ")
newsvector=vectorizer.transform([news])
prediction=model.predict(newsvector)
print("\nPrediction:",prediction[0])