import pandas as pd
import matplotlib.pyplot as plt


#remove lines with tbd
data = pd.read_csv('data.csv')
data = pd.DataFrame(data)
data = data[data["User score"].astype('str').str.contains('0') == False]
data["User score"] = pd.to_numeric(data["User score"]).astype('Int64')
data["Meta score"] = pd.to_numeric(data["Meta score"]).astype('Int64')
data = data.drop('Unnamed: 0', axis=1)

#show Meta and User score graphic
plt.plot(data["Meta score"])
plt.plot(data["User score"], alpha=0.6)
plt.show()

#find the most common game grade
print("Most common Meta score:" + str(data["Meta score"].value_counts().idxmax()))
print("Most common User score:" + str(data["User score"].value_counts().idxmax()))

print("Mean of " + str(data.mean(numeric_only=True)))



