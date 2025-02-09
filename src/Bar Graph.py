import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:/Users/USER/Documents/3rd year 2nd sem/Data Analytics/Assignment_2_Data_Analytics/data/bar_assignment.csv")

data_dict = {}
for _, row in df.iterrows():
    label = row["LABEL"]
    count = row["COUNT"]
    if label not in data_dict:
        data_dict[label] = {"yes": 0, "no": 0}
    if count == 1:
        data_dict[label]["yes"] += 1
    else:
        data_dict[label]["no"] += 1

departments = list(data_dict.keys())
yes_responses = [data_dict[label]["yes"] for label in departments]
no_responses = [data_dict[label]["no"] for label in departments]

y_positions = np.arange(len(departments))

plt.figure(figsize=(10, 6))

bars_no = plt.barh(y_positions, no_responses, color='red', label="No")
bars_yes = plt.barh(y_positions, yes_responses, left=no_responses, color='blue', label="Yes")

plt.xticks(fontsize=10)
plt.yticks(y_positions, departments, fontsize=10)

plt.title("Student Agreement on Quantum Physics and Interdimensional Communication", fontsize=14, pad=50)
plt.text(0, len(departments) - 0.05, "Legend Here", fontsize=12, fontweight='bold', va='center')
plt.legend(fontsize=10, title_fontsize=12, loc='upper center', bbox_to_anchor=(0.3, 1.1), ncol=2, frameon=False)
plt.xlabel("Number of Students", fontsize=12)
plt.ylabel("Departments", fontsize=12)

for i in range(len(departments)):
    if no_responses[i] > 0:
        plt.text(no_responses[i] / 2, y_positions[i], str(no_responses[i]),
                 va='center', ha='center', fontsize=10, color='white')
    if yes_responses[i] > 0:
        plt.text(no_responses[i] + yes_responses[i] / 2, y_positions[i],
                 str(yes_responses[i]), va='center', ha='center', fontsize=10, color='white')

plt.show()