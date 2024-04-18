import json

# Data from the Python script
nodes = {
    'I1': {'x': -8, 'y': 5},
    'I2': {'x': -8, 'y': 9},
    'I3': {'x': -4.5, 'y': 9},
    'I4': {'x': -2, 'y': 9},
    'I6': {'x': 1.5, 'y': 8},
    'I7': {'x': 3.5, 'y': 6},
    'G4': {'x': -3.5, 'y': 4.5},
    'G3': {'x': -1, 'y': 6},
    'G1': {'x': 0.5, 'y': 3.5},
    'G2': {'x': 4, 'y': 2},
    'G5': {'x': -5, 'y': 2.5},
}

edges = [
    ('I1', 'I2', 7),
    ('I2', 'I1', 7),
    ('I2', 'I3', 10),
    ('I3', 'I2', 10),
    ('I3', 'I4', 15),
    ('I4', 'I3', 15),
    ('I4', 'I6', 12),
    ('I6', 'I4', 12),
    ('I6', 'I7', 13),
    ('I7', 'I6', 13),
    ('G5', 'I1', 12),
    ('I1', 'G5', 12),
    ('G4', 'I1', 11),
    ('I1', 'G4', 11),
    ('G4', 'I3', 7),
    ('I3', 'G4', 7),
    ('G4', 'I4', 7),
    ('I4', 'G4', 7),
    ('G3', 'I4', 5),
    ('I4', 'G3', 5),
    ('G3', 'I6', 6),
    ('I6', 'G3', 6),
    ('G1', 'I6', 7),
    ('I6', 'G1', 7),
    ('G2', 'I7', 12),
    ('I7', 'G2', 12),
]

# Converting to JSON format
graph_json = {
    "nodes": [{**{"id": node}, **nodes[node]} for node in nodes],
    "edges": [{"from": edge[0], "to": edge[1], "weight": edge[2]} for edge in edges]
}


# Save to a JSON file
json_path = 'graph_data.json'  # This will save the file in the current directory
with open(json_path, 'w') as json_file:
    json.dump(graph_json, json_file, indent=4)


