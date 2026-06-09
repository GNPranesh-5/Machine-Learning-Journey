import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/loandata.csv")

approvalcount = df["Approval"].value_counts()

approvalcount.plot(kind="bar")

plt.title("Loan Approval Distribution")
plt.xlabel("Approval")
plt.ylabel("Count")

plt.show()