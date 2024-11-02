# main.py

from graph import Graph
from graph_test import TestGraph
import unittest

# Create an instance of Graph
graph = Graph()

# Add nodes to the graph
graph.add_node("Jasmine")
graph.add_node("Ada")
graph.add_node("Lydia")

# Create edges in the graph
graph.create_edge("Jasmine", "Ada")
graph.create_edge("Ada", "Lydia")

# Print the state of the graph
print("Graph after adding nodes and edges:")
print(graph)

Check if nodes exist in the graph
print("Does 'Jasmine' exist in the graph?", graph.has_node("Jasmine"))
print("Does 'John' exist in the graph?", graph.has_node("John"))

# Check if edges exist in the graph
print("Does edge exist between 'Jasmine' and 'Ada'?", graph.has_edge("Jasmine", "Ada"))
print("Does edge exist between 'Ada' and 'Lydia'?", graph.has_edge("Ada", "Lydia"))

# Remove an edge from the graph
graph.remove_edge("Jasmine", "Ada")

# Print the state of the graph after removing an edge
print("Graph after removing an edge:")
print(graph)

# Remove a node from the graph
graph.remove_node("Jasmine")

# Print the state of the graph after removing a node
print("Graph after removing a node:")
print(graph)

if __name__ == '__main__':
    unittest.main()