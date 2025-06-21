from MaximumIndependentSetGreedyApproximation import greedyApproximation
from MaximumIndependentSetSimulatedAnnealing import maximumIndependentAnnealing
import networkx as nx


def create_max_cut_graph(num_nodes, edge_prob):

    G = nx.erdos_renyi_graph(num_nodes, edge_prob)  # Creates a random Erdős–Rényi graph

    return G

repetitions = 100


points = 100
graph = create_max_cut_graph(points, 0.4)
edges = graph.edges()
edges = list(edges)





greedyAvg = 0
annealAvg = 0
greedyMax = 0
annealMax = 0

for i in range(repetitions):
    greedyResult = greedyApproximation(edges, points)
    annealResult = maximumIndependentAnnealing(edges,points)


    greedyAvg = greedyAvg + greedyResult
    annealAvg = annealAvg + annealResult


    if greedyResult > greedyMax:
        greedyMax = greedyResult
    if annealResult > annealMax:
        annealMax = annealResult

    print(i)


greedyAvg = greedyAvg / repetitions
annealAvg = annealAvg / repetitions

print("GreedyAvg: ", greedyAvg)
print("AnnealAvg: ", annealAvg)


print("Best Greedy: ", greedyMax)
print("Best Anneal: ", annealMax)