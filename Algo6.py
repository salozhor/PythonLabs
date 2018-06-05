import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.traversal.edgedfs import helper_funcs, edge_dfs

G=nx.Graph()


"""
Node describing
"""
G.add_node('a')
G.add_node('b')
G.add_node('c')
G.add_node('d')
G.add_node('g')
G.add_node('f')
G.add_node('s')
G.add_node('t')

"""
Edge describing
"""
G.add_edge('s','a')
G.add_edge('s','c')
G.add_edge('s','d')
G.add_edge('a','b')
G.add_edge('a','f')
G.add_edge('a','g')
G.add_edge('b','c')
G.add_edge('b','g')
G.add_edge('c','t')
G.add_edge('d','f')
G.add_edge('f','g')
G.add_edge('g','t')
