import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

data = pd.read_csv('C:/Users/USER/Documents/3rd year 2nd sem/Data Analytics/Assignment_2_Data_Analytics/data/networks_assignment.csv', index_col=0)

G = nx.Graph()

for label in data.index:
    G.add_node(label)

for i, label1 in enumerate(data.index):
    for j, label2 in enumerate(data.columns):
        if data.iloc[i, j] > 0:
            G.add_edge(label1, label2)

central_nodes = ['D', 'F', 'I', 'N', 'S']
outer_nodes = [node for node in G.nodes if node not in central_nodes]

central_pos = {
    'D': (0, 1),
    'F': (0.951, 0.309),
    'I': (0.588, -0.809),
    'N': (-0.588, -0.809),
    'S': (-0.951, 0.309)
}

outer_pos = nx.circular_layout(outer_nodes, scale=2)

pos = {**central_pos, **outer_pos}

node_colors = {
    'D': 'blue', 'F': 'blue', 'I': 'blue', 'N': 'blue', 'S': 'blue',
    'BIH': 'green', 'GEO': 'green', 'ISR': 'green', 'MNE': 'green', 'SRB': 'green', 'CHE': 'green', 'TUR': 'green', 'UKR': 'green', 'GBR': 'green', 'AUS': 'green', 'HKG': 'green', 'ASU': 'green',
    'AUT': 'yellow', 'BEL': 'yellow', 'BGR': 'yellow', 'HRV': 'yellow', 'CZE': 'yellow', 'EST': 'yellow', 'FRA': 'yellow', 'DEU': 'yellow', 'GRC': 'yellow', 'HUN': 'yellow', 'IRL': 'yellow', 'ITA': 'yellow', 'LVA': 'yellow', 'LUX': 'yellow', 'NLD': 'yellow', 'PRT': 'yellow', 'ROU': 'yellow', 'SVK': 'yellow', 'SVN': 'yellow', 'ESP': 'yellow'
}

nx.draw_networkx_nodes(G, pos, node_size=700, node_color=[node_colors[node] for node in G.nodes])
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=12)

plt.title("Network Graph")
plt.axis('off')
plt.show()