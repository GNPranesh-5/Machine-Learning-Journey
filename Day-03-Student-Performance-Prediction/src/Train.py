import pandas as pd  
import pickle
from sklearn.linear_model import LinearRegression
df=pd.read_csv("../data/studentdata.csv")
x=df[["StudyHours","Attendance","Assignments"]]
y=df["Score"]

model=LinearRegression()
model.fit(x,y)

with open("../models/studentmodel.pkl","wb") as file:
    pickle.dump(model,file)
    
print("Student model saved successfully")