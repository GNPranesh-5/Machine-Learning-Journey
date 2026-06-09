import pandas as pd  
import pickle
from sklearn.linear_model import LogisticRegression

df=pd.read_csv("../data/loandata.csv")

x=df[["Income","CreditScore","LoanAmount"]]
y=df["Approval"]
model=LogisticRegression()
model.fit(x,y)

with open("../models/loanmodel.pkl","wb") as file:
    pickle.dump(model,file)
print("Loan approval model saved successfully")