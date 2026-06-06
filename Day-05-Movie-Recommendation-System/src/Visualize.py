import pandas as pd  
import matplotlib.pyplot as plt  

df=pd.read_csv("../data/movies.csv")
genrecount=df["Genre"].value_counts()
plt.figure(figsize=(8,5))
genrecount.plot(kind="bar")
plt.title("Movies by Genre")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.show()