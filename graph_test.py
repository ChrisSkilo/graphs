# graph_test.py

import unittest
from graph import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def tearDown(self):
        self.graph = Graph()
    
    def test_instantiate_graph(self):
        self.assertEqual(len(self.graph.adjacency_list), 0)

    def test_add_node(self):
        self.graph.add_node("Jasmine")
        self.assertEqual(len(self.graph.adjacency_list["Jasmine"]), 0)

    def test_has_node_false(self):
        self.assertFalse(self.graph.has_node("Ada"))

    def test_has_node_true(self):
        self.graph.add_node("Jasmine")
        self.assertTrue(self.graph.has_node("Jasmine"))
    
    def test_create_edge(self):
        self.graph.add_node("Jasmine")
        self.graph.add_node("Ada")
        self.graph.create_edge("Jasmine", "Ada")
        self.assertTrue("Ada" in self.graph.adjacency_list["Jasmine"])
        self.assertTrue("Jasmine" in self.graph.adjacency_list["Ada"])
    
    def test_has_edge_true(self):
        self.graph.add_node("Jasmine")
        self.graph.add_node("Ada")
        self.graph.create_edge("Jasmine", "Ada")
        self.assertTrue(self.graph.has_edge("Jasmine", "Ada"))
    
    def test_remove_edge(self):
        self.graph.add_node("Jasmine")
        self.graph.add_node("Ada")
        self.graph.create_edge("Jasmine", "Ada")
        self.graph.remove_edge("Jasmine", "Ada")
        self.assertFalse(self.graph.has_edge("Ada", "Jasmine"))
    
    def test_remove_node(self):
        self.graph.add_node("Jasmine")
        self.graph.add_node("Ada")
        self.graph.create_edge("Jasmine", "Ada")
        self.graph.remove_node("Jasmine")
        self.assertFalse(self.graph.has_edge("Ada", "Jasmine"))
        self.assertFalse(self.graph.has_node("Jasmine"))


    
    
    
