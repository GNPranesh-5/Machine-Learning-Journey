import pandas as pd  
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans

df=pd.read_csv("../data/customerdata.csv")
x=df[["Income","SpendingScore"]]
model=KMeans(n_clusters=3,random_state=42)
df["Cluster"]=model.fit_predict(x)
plt.scatter(df["Income"],df["SpendingScore"],c=df["Cluster"])
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.show()