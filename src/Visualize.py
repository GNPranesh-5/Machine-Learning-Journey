import matplotlib.pyplot as plt  
import pandas as pd  
df = pd.read_csv("../data/HouseData.csv")
plt.scatter(df["Size"],df["Price"])
plt.xlabel("HouseSize")
plt.ylabel("Price")
plt.title("Size vs Price")
plt.show()