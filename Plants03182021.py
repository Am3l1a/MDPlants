import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel("18Mar2021.xlsx")
#Counting toxic plants and graphing the results of the count
CTox = data.value_counts("Toxicity")
plt.plot(CTox)
plt.ylabel("Number of Plants")
plt.xlabel("Toxicity Status")
plt.title("How Many Plants in MD are Toxic?")
#plt.show()

df = pd.DataFrame(data)
SevTox = df[df["Toxicity"]=="Severe"]
#CSevTox = SevTox.value_counts("Toxicity")
#print(CSevTox)
