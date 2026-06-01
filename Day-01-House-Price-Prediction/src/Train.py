import pandas as pd
import matplotlib.pyplot as plt  
import pickle 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
df=pd.read_csv("../data/HouseData.csv")
print(df.head())
x=df[["Size","Bedrooms"]]
y=df["Price"]
x_train,x_test,y_train,y_test=train_test_split(
    x,y,
    test_size=0.2,
    random_state=42
)
model=LinearRegression()
model.fit(x_train,y_train)
prediction=model.predict(x_test)
mae=mean_absolute_error(y_test,prediction)
print("Mean Absolute Error: ",mae)
with open("../models/HouseModel.pkl","wb") as file:
    pickle.dump(model,file)
print("Model Saved successfully as HouseModel.pk")
