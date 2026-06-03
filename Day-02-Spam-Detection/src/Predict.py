import pickle

with open("../models/spammodel.pkl","rb") as file:
    model=pickle.load(file)
with open("../models/vectorizer.pkl","rb") as file:
    vectorizer=pickle.load(file)
message=input("Enter message: ")
msgvector=vectorizer.transform([message])
prediction=model.predict(msgvector)
print("\nPrediction:",prediction[0])