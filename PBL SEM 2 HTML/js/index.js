// // Define nodes and edges
// var nodesArray = [
//     {id: 'I1', label: 'I1', x: -800, y: 500, color: 'lightblue'},
//     {id: 'I2', label: 'I2', x: -800, y: 900, color: 'lightblue'},
//     {id: 'I3', label: 'I3', x: -450, y: 900, color: 'lightblue'},
//     {id: 'I4', label: 'I4', x: -200, y: 900, color: 'lightblue'},
//     {id: 'I6', label: 'I6', x: 150, y: 800, color: 'lightblue'},
//     {id: 'I7', label: 'I7', x: 350, y: 600, color: 'lightblue'},
//     {id: 'G1', label: 'G1', x: 50, y: 350, color: 'lightgreen'},
//     {id: 'G2', label: 'G2', x: 400, y: 200, color: 'lightgreen'},
//     {id: 'G3', label: 'G3', x: -100, y: 600, color: 'lightgreen'},
//     {id: 'G4', label: 'G4', x: -350, y: 450, color: 'lightgreen'},
//     {id: 'G5', label: 'G5', x: -500, y: 250, color: 'lightgreen'}
//     // ... add other nodes
// ];

// var edgesArray = [
//     {from: 'I1', to: 'I2', label: '7', arrows: 'to'},
//     {from: 'I2', to: 'I3', label: '10', arrows: 'to'},
//     {from: 'I3', to: 'I4', label: '15', arrows: 'to'},
//     {from: 'I4', to: 'I6', label: '12', arrows: 'to'},
//     {from: 'I6', to: 'I7', label: '13', arrows: 'to'},
//     {from: 'G5', to: 'I1', label: '12', arrows: 'to'},
//     {from: 'G4', to: 'I1', label: '11', arrows: 'to'},
//     {from: 'G4', to: 'I3', label: '7', arrows: 'to'},
//     {from: 'G3', to: 'I4', label: '5', arrows: 'to'},
//     {from: 'G3', to: 'I6', label: '6', arrows: 'to'},
//     {from: 'G1', to: 'I6', label: '7', arrows: 'to'},
//     {from: 'G2', to: 'I7', label: '12', arrows: 'to'}
//     // ... add other edges
// ];

// // Convert nodes and edges to vis.js DataSet
// var nodes = new vis.DataSet(nodesArray);
// var edges = new vis.DataSet(edgesArray);

// // Create a network
// var container = document.getElementById('network');
// var data = {
//     nodes: nodes,
//     edges: edges
// };
// var options = {
//     physics: false, // Disable physics
//     edges: {
//         font: {
//             align: 'top'
//         }
//     }
// };
// var network = new vis.Network(container, data, options);

// // Dijkstra's algorithm to find the shortest path
// // (This will be a pseudo-code implementation as the algorithm can be complex to write from scratch)
// function dijkstraAlgorithm(startNode, endNode) {
//     // ... your Dijkstra's implementation here
//     // Returns an array of node IDs representing the shortest path
// }

// // Compute the shortest path from I1 to I7
// var shortestPath = dijkstraAlgorithm('I1', 'I7');

// // Highlight the shortest path on the graph
// // (Pseudo-code: The actual implementation will depend on how you've set up Dijkstra's algorithm)
// shortestPath.forEach((nodeId, index) => {
//     if (index < shortestPath.length - 1) {
//         var edgeId = edges.get({
//             filter: function(edge) {
//                 return edge.from === nodeId && edge.to === shortestPath[index + 1];
//             }
//         })[0].id;
//         edges.update({id: edgeId, color: 'red', width: 3});
//     }
// });
// nodes.update(shortestPath.map(nodeId => ({id: nodeId, color: 'green'})));
