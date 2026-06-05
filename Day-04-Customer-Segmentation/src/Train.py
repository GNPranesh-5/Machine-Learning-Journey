import pandas as pd  
from sklearn.cluster import KMeans

df=pd.read_csv("../data/customerdata.csv")
x=df[["Income","SpendingScore"]]

model=KMeans(n_clusters=3,random_state=42)
model.fit(x)
df["Cluster"]=model.labels_
print(df.head())

print("\nCustomer Segmentation Completed")