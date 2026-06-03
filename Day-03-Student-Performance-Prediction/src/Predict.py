import pickle
import pandas as pd  

with open("../models/studentmodel.pkl","rb") as file:
    model=pickle.load(file)

studyhours=float(input("Enter study hours: "))
attendance=float(input("Enter attendance (%): "))
assignments=int(input("Enter assigments completed: "))

data=pd.DataFrame({
    "StudyHours":[studyhours],
    "Attendance":[attendance],
    "Assignments":[assignments]
})

prediction=model.predict(data)
print("\nPredicted Score:",round(prediction[0],2))