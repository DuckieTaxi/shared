import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import asyncio

# CRETE Graph
G=nx.Graph()
# MAKING NODE
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_node('F')
G.add_node('G')
G.add_node('H')
G.add_node('K')
G.add_node('L')
G.add_node('E')
# MAKE EDGE IN GRAPH
G.add_edge('A', 'B', weight=30)
G.add_edge('A', 'C', weight=5)
G.add_edge('A', 'D', weight=26)
G.add_edge('A', 'K', weight=14)
G.add_edge('B', 'C', weight=20)
G.add_edge('B', 'D', weight=16)
G.add_edge('B', 'E', weight=15)
G.add_edge('B', 'F', weight=28)
G.add_edge('B', 'G', weight=19)
G.add_edge('B', 'H', weight=10)
G.add_edge('C', 'D', weight=8)
G.add_edge('C', 'E', weight=41)
G.add_edge('C', 'F', weight=50)
G.add_edge('C', 'H', weight=44)
G.add_edge('D', 'E', weight=39)
G.add_edge('D', 'F', weight=13)
G.add_edge('D', 'K', weight=26)
G.add_edge('F', 'G', weight=2)
G.add_edge('G', 'K', weight=15)
G.add_edge('G', 'D', weight=10)
G.add_edge('G', 'K', weight=28)
G.add_edge('L', 'K', weight=8)
G.add_edge('L', 'F', weight=8)


class AlgoritmsWithGraphs:
    def algoritm_deikstra(self, end, start):
        path = ""
        for el in nx.bidirectional_dijkstra(G, start, end)[1]:
            path += el + ' '
        return path

