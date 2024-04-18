import matplotlib.pyplot as plt
import networkx as nx

# Crearea unui grafic orientat pentru a reprezenta harta
G = nx.DiGraph()

# Adăugarea nodurilor și muchiilor în graficul G cu greutățile lor
G.add_edge('I1', 'I2', weight=7)
G.add_edge('I2', 'I1', weight=7)
G.add_edge('I2', 'I3', weight=10)
G.add_edge('I3', 'I2', weight=10)
G.add_edge('I3', 'I4', weight=15)
G.add_edge('I4', 'I3', weight=15)
G.add_edge('I4', 'I6', weight=12)
G.add_edge('I6', 'I4', weight=12)
G.add_edge('I6', 'I7', weight=13)
G.add_edge('I7', 'I6', weight=13)
G.add_edge('G5', 'I1', weight=12)
G.add_edge('I1', 'G5', weight=12)
G.add_edge('G4', 'I1', weight=11)
G.add_edge('I1', 'G4', weight=11)
G.add_edge('G4', 'I3', weight=7)
G.add_edge('I3', 'G4', weight=7)
G.add_edge('G4', 'I4', weight=7)
G.add_edge('I4', 'G4', weight=7)
G.add_edge('G3', 'I4', weight=5)
G.add_edge('I4', 'G3', weight=5)
G.add_edge('G3', 'I6', weight=6)
G.add_edge('I6', 'G3', weight=6)
G.add_edge('G1', 'I6', weight=7)
G.add_edge('I6', 'G1', weight=7)
G.add_edge('G2', 'I7', weight=12)
G.add_edge('I7', 'G2', weight=12)

pos = {
    'I1': (-8, 5),
    'I2': (-8, 9),
    'I3': (-4.5, 9),
    'I4': (-2, 9),
    'I6': (1.5, 8),
    'I7': (3.5, 6),
    'G4': (-3.5, 4.5),
    'G3': (-1, 6),
    'G1': (0.5, 3.5),
    'G2': (4, 2),
    'G5': (-5, 2.5),
}

# Set the figure background to black
plt.figure(figsize=(8, 6))
plt.gca().set_facecolor('#000000')

# Adjust the draw function to improve visibility on a black background
nx.draw(G, pos, with_labels=True, font_color='white', node_color='skyblue', edge_color='green', node_size=2000, width=2)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='#006600')

# Highlighting the shortest path
start_node = 'I1'
end_node = 'I7'
path = nx.dijkstra_path(G, source=start_node, target=end_node)
print(f"Cel mai scurt drum de la {start_node} la {end_node} este: {path}")

path_edges = list(zip(path, path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='blue')

plt.show()
