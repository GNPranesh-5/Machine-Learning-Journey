import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/news.csv")

count = df["label"].value_counts()

count.plot(kind="bar")

plt.title("Fake vs Real News")

plt.xlabel("Category")
plt.ylabel("Count")

plt.show()