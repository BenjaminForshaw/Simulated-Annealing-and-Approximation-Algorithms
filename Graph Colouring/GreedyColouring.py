import networkx as nx
import matplotlib.pyplot as plt
import math
import random
import time

def greedyColour(edgeList,pointNum):
    start_time = time.perf_counter()

    colours = [0]

    nodeAllocation = []
    for i in range(pointNum):
        nodeAllocation.append(-1)

    '''
    For each node:
    1. Check each node surrounding it for 'not allowed' colours.
    2. Label the node with the oldest 'allowed' colour. Create a new colour if needed.
    
    '''


    for i in range(pointNum):

        bannedColours = []
        for j in range(len(edgeList)):
            if edgeList[j][0] == i:
                if nodeAllocation[edgeList[j][1]] != -1:
                    if nodeAllocation[edgeList[j][1]] not in bannedColours:
                        bannedColours.append(nodeAllocation[edgeList[j][1]])
            elif edgeList[j][1] == i:
                if nodeAllocation[edgeList[j][0]] != -1:
                    if nodeAllocation[edgeList[j][0]] not in bannedColours:
                        bannedColours.append(nodeAllocation[edgeList[j][0]])


        if len(bannedColours) == len(colours):
            lastColour = len(colours)
            colours.append(lastColour)


        labelled = False
        for x in range(len(colours)):
            if colours[x] not in bannedColours:
                if labelled == False:
                    nodeAllocation[i] = colours[x]


    end_time = time.perf_counter()
    run_time = end_time - start_time
    return len(colours)




















def create_graph_colour_graph(num_nodes, edge_prob):
    G = nx.erdos_renyi_graph(num_nodes, edge_prob)  # Creates a random Erdős–Rényi graph
    return G



points = 500
graph = create_graph_colour_graph(points, 0.4)
edges = graph.edges()
edges = list(edges)
  # View the edges of the generated graph









