import plotly.graph_objects as go
import pandas as pd

# Load the data from CSV file
df = pd.read_csv("C:/Users/USER/Documents/3rd year 2nd sem/Data Analytics/Assignment_2_Data_Analytics/data/sankey_assignment.csv")

# Define the labels for the Sankey diagram
left_labels = df.columns[1:9]  
right_labels = df.columns[9:]  
middle_labels = df["LABEL"].tolist()

# Combine all labels into a single list
labels = list(left_labels) + middle_labels + list(right_labels)
label_to_index = {label: i for i, label in enumerate(labels)}

# Initialize lists for sources, targets, and values
sources = []
targets = []
values = []

# Populate the sources, targets, and values lists
for _, row in df.iterrows():
    mid_label = row["LABEL"]
   
    for left in left_labels:
        flow_value = row[left]
        if flow_value > 0:
            sources.append(label_to_index[left])
            targets.append(label_to_index[mid_label])
            values.append(flow_value)
  
    for right in right_labels:
        flow_value = row[right]
        if flow_value > 0:
            sources.append(label_to_index[mid_label])
            targets.append(label_to_index[right])
            values.append(flow_value)

# Define colors for the nodes
colors = {
    "OMP": "#20b2aa",
    "PS": "#ffa07a",
    "CNP": "#ff8c00",
    "RGS": "#ba55d3",
    "NRP": "#ff6ab4",
    "NCDM": "#ffd701",
    "NMCCC": "#8fbc8f",
    "PEC": "#02ced1",
    "S": "#87cefa",
    "I": "#00bfff",
    "D": "#5f9ea0",
    "F": "#4782b4",
    "N": "#6395ed",
    "Aca": "#97fb98",
    "Reg": "#3cb371",
    "Oth": "#90ee8f"
}

# Assign colors to nodes and make labels bold
node_colors = [colors[label] for label in labels]
bold_labels = [f"<b>{label}</b>" for label in labels]

# Create the Sankey diagram
fig = go.Figure(go.Sankey(
    node=dict(
        pad=20,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=bold_labels,  
        color=node_colors
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values,
        color=[node_colors[src] for src in sources]  
    )
))

# Update layout and display the diagram
fig.update_layout(
    title_text="Sankey Diagram",
    font_size=18
)

fig.show()