import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Nodes: Regional powers and Afghanistan
nodes = [
    "China", "Pakistan", "India", "Afghanistan",
    "BRI/CPEC", "Uyghur Militants", "Refugees", "Strategic Aid", "TTP/BLA"
]

for node in nodes:
    G.add_node(node)

# Core influence triangle
edges = [
    ("China", "Afghanistan"),
    ("Pakistan", "Afghanistan"),
    ("India", "Afghanistan"),
    ("China", "BRI/CPEC"),
    ("BRI/CPEC", "Afghanistan"),
    ("China", "Uyghur Militants"),
    ("Afghanistan", "Uyghur Militants"),
    ("Pakistan", "TTP/BLA"),
    ("Afghanistan", "TTP/BLA"),
    ("India", "Strategic Aid"),
    ("Strategic Aid", "Afghanistan"),
    ("Pakistan", "Refugees"),
    ("Afghanistan", "Refugees")
]

G.add_edges_from(edges)

# Create layout and draw
plt.figure(figsize=(14, 10))
pos = nx.spring_layout(G, seed=21)
nx.draw_networkx_nodes(G, pos, node_size=2500, node_color='lightyellow', edgecolors='black')
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=15, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
plt.title("Triangular Influence Dynamics: China, Pakistan, and India Shaping Afghanistan", fontsize=14)
plt.axis('off')
plt.tight_layout()

# Save output
plt.savefig("axis_of_leverage_map.png", dpi=300)
