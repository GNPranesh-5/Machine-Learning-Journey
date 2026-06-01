import pickle
from sklearn.linear_model import LinearRegression

with open("../models/HouseModel.pkl","rb") as file:
    model = pickle.load(file)
size=2500
Bedrooms=4  
prediction = model.predict([[size, Bedrooms]])
print("\nHouse Details")
print("Size:", size)
print("Bedrooms:", Bedrooms)

print("\nPredicted Price:", round(prediction[0], 2), "Lakhs")
