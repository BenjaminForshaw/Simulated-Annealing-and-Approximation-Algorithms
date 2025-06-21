from SimulatedAnnealingImplementation import simulatedAnnealingMaximumCut
from GWMaximumCutImplementation import GoemansWilliamsonMaxCut
import networkx as nx

def create_max_cut_graph(num_nodes, edge_prob):

    G = nx.erdos_renyi_graph(num_nodes, edge_prob)  # Creates a random Erdős–Rényi graph

    return G


''' Amount of points in the graph. '''
points = 10
graph = create_max_cut_graph(points, 0.4)
edges = graph.edges()
edges = list(edges)
  # View the edges of the generated graph



bestAnneal = 0
bestGW = 0

annealingAverage = 0
gwAverage = 0
repetitions = 100


for i in range(repetitions):
    Annealresult = simulatedAnnealingMaximumCut(edges,points)
    GWoutput = GoemansWilliamsonMaxCut(edges, points)

    annealingAverage += Annealresult
    gwAverage += GWoutput

    if Annealresult > bestAnneal:
        bestAnneal = Annealresult
    if GWoutput > bestGW:
        bestGW = GWoutput





annealingAverage = annealingAverage/repetitions
gwAverage = gwAverage/repetitions

print("Simulated Annealing Average Output: ")
print(annealingAverage)
print()
print("Goemans & Williamson Average Output: ")
print(gwAverage)


print()
print("Best Annealing: ")
print(bestAnneal)
print()
print("Best GW : ")
print(bestGW)