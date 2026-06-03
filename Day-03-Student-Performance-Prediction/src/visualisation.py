import pandas as pd  
import matplotlib.pyplot as plt  

df=pd.read_csv("../data/studentdata.csv")

plt.scatter(df["StudyHours"],df["Score"])

plt.xlabel("StudyHours")
plt.ylabel("Score")
plt.title("Study Hours vs Score")

plt.show()