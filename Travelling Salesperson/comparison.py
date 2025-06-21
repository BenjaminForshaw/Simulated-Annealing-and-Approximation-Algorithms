from TravellingSalesAnneal import annealAlg
from TravellingSalesApprox import approxAlg
import networkx as nx
import matplotlib.pyplot as plt
import random
import math




nodes = 100
Graph = nx.complete_graph(nodes)

pos = {}

for i in Graph.nodes:
    pos[i] = (random.random(), random.random())


def pythag_distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

for i,j in Graph.edges:
    (x1,y1)=pos[i]
    (x2,y2)=pos[j]
    Graph.edges[i,j]['length'] = pythag_distance(x1,y1,x2,y2)



bestAnneal=1000000
bestApprox=1000000
avgAnneal=0
avgApprox=0

repetitions = 100
for i in range(repetitions):

    anneal = annealAlg(Graph,pos)
    approx = approxAlg(Graph,pos)
    avgAnneal = avgAnneal + anneal
    avgApprox = avgApprox + approx
    if anneal<bestAnneal:
        bestAnneal = anneal
    if approx<bestApprox:
        bestApprox = approx

    print(i)


print("Average anneal: ", avgAnneal/repetitions)
print("Average approx: ", avgApprox/repetitions)
print("Best anneal: ", bestAnneal)
print("Best approx: ", bestApprox)