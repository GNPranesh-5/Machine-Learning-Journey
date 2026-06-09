import pickle
import pandas as pd  

with open("../models/loanmodel.pkl","rb") as file:
    model=pickle.load(file)

income=float(input("Enter income: "))
creditscore=float(input("Enter credit score: "))
loanamount=float(input("Enter loan amount: "))

data=pd.DataFrame({
    "Income":[income],
    "CreditScore":[creditscore],
    "LoanAmount":[loanamount]
})

prediction=model.predict(data)[0]

if prediction==1:
    print("\nLoan Approved")
else:
    print("\nLoan Rejected")