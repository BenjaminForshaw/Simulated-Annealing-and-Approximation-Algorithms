import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import math
import random

from GreedyColouring import greedyColour
from AnnealColouring import annealColour


def create_graph_colour_graph(num_nodes, edge_prob):
    Graph = nx.erdos_renyi_graph(num_nodes, edge_prob)  # Creates a random Erdős–Rényi graph
    return Graph


''' Amount of points in the graph. '''
points = 100
probability = 0.4
repetitions = 100
graph = create_graph_colour_graph(points, probability)
edges = graph.edges()
edges = list(edges)


bestAnneal = 10000
bestG = 10000
annealingAverage = 0
gAverage = 0



for i in range(repetitions):
    Annealresult = annealColour(edges,points)
    Gresult = greedyColour(edges, points)

    annealingAverage += Annealresult
    gAverage += Gresult

    if Annealresult < bestAnneal:
        bestAnneal = Annealresult
    if Gresult < bestG:
        bestG = Gresult

    print(i)


annealingAverage = annealingAverage/repetitions
gAverage = gAverage/repetitions

print("Simulated Annealing Average Output: ")
print(annealingAverage)
print()
print("Greedy algorithm Average Output: ")
print(gAverage)


print()
print("Best Annealing: ")
print(bestAnneal)
print()
print("Best Greedy: ")
print(bestG)


