import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from CSV file
df = pd.read_csv("C:/Users/USER/Documents/3rd year 2nd sem/Data Analytics/Assignment_2_Data_Analytics/data/bar_assignment.csv")

# Initialize a dictionary to store the data
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

# Extract the departments and their responses
departments = list(data_dict.keys())
yes_responses = [data_dict[label]["yes"] for label in departments]
no_responses = [data_dict[label]["no"] for label in departments]

# Define the y positions for the bars
y_positions = np.arange(len(departments))

# Create the bar graph
plt.figure(figsize=(10, 6))

# Plot the 'No' responses
bars_no = plt.barh(y_positions, no_responses, color='red', label="No")
# Plot the 'Yes' responses
bars_yes = plt.barh(y_positions, yes_responses, left=no_responses, color='blue', label="Yes")

# Set the x and y axis labels and ticks
plt.xticks(fontsize=10)
plt.yticks(y_positions, departments, fontsize=10)

# Set the title and legend
plt.title("Student Agreement on Quantum Physics and Interdimensional Communication", fontsize=14, pad=50)
plt.text(0, len(departments) - 0.05, "Legend Here", fontsize=12, fontweight='bold', va='center')
plt.legend(fontsize=10, title_fontsize=12, loc='upper center', bbox_to_anchor=(0.3, 1.1), ncol=2, frameon=False)
plt.xlabel("Number of Students", fontsize=12)
plt.ylabel("Departments", fontsize=12)

# Add text labels to the bars
for i in range(len(departments)):
    if no_responses[i] > 0:
        plt.text(no_responses[i] / 2, y_positions[i], str(no_responses[i]),
                 va='center', ha='center', fontsize=10, color='white')
    if yes_responses[i] > 0:
        plt.text(no_responses[i] + yes_responses[i] / 2, y_positions[i],
                 str(yes_responses[i]), va='center', ha='center', fontsize=10, color='white')

# Display the plot
plt.show()