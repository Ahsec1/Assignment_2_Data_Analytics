import matplotlib.pyplot as plt
import numpy as np

departments = ["Computer Science", "Physics", "Engineering", "Biology", "Mathematics"]
yes_responses = [3, 2, 1, 2, 5]
no_responses = [2, 2, 0, 1, 5]

y_positions = np.arange(len(departments))

plt.figure(figsize=(10, 6))

bars_no = plt.barh(y_positions, no_responses, color='red', label="No")
bars_yes = plt.barh(y_positions, yes_responses, left=no_responses, color='blue', label="Yes")

plt.xticks(fontsize=10)
plt.yticks(y_positions, departments, fontsize=10)

plt.title("Student Agreement on Quantum Physics and Interdimensional Communication", fontsize=14, pad=50)
plt.text(0, len(departments) + -0.05, "Legend Here", fontsize=12, fontweight='bold', va='center')
plt.legend(fontsize=10, title_fontsize=12, loc='upper center', bbox_to_anchor=(0.3, 1.1), ncol=2, frameon=False)
plt.xlabel("Number of Students", fontsize=12)
plt.ylabel("Departments", fontsize=12)

for i in range(len(departments)):
    if no_responses[i] > 0:
        plt.text(no_responses[i] / 2, y_positions[i], str(no_responses[i]), va='center', ha='center', fontsize=10, color='white')
    if yes_responses[i] > 0:
        plt.text(no_responses[i] + yes_responses[i] / 2, y_positions[i], str(yes_responses[i]), va='center', ha='center', fontsize=10, color='white')

plt.show()