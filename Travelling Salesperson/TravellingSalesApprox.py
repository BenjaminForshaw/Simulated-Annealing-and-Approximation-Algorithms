import random
import matplotlib.pyplot as plt
import networkx as nx
import math
import time



def approxAlg(completeGraph, positions):
    start_time = time.perf_counter()

    #nx.draw(G, pos=positions)
    #plt.show()


    minimumSpanningTree = nx.minimum_spanning_tree(completeGraph, weight='length')
    #nx.draw(T, pos=positions)
    #plt.show()


    odd_degree_nodes = []
    node_colours = []
    for i in minimumSpanningTree.nodes:

        if minimumSpanningTree.degree(i) % 2:
            odd_degree_nodes.append(i)
        node_colours.append(minimumSpanningTree.degree(i) % 2)


    #nx.draw(T, pos=positions, node_color=node_colours)
    #plt.show()

    for i,j in completeGraph.edges:
        completeGraph.edges[i,j]['neg_length'] = - completeGraph.edges[i,j]['length']

    matching = nx.max_weight_matching(completeGraph.subgraph(odd_degree_nodes), maxcardinality=True, weight ='neg_length')

    #nx.draw(G.edge_subgraph(matching), pos=positions)
    #plt.show()

    multiGraph = nx.MultiGraph()

    multiGraph.add_nodes_from(range(len(completeGraph.nodes)))
    multiGraph.add_edges_from(minimumSpanningTree.edges())
    multiGraph.add_edges_from(matching)


    #nx.draw(M, pos=positions)
    #plt.show()


    initial_tour = list(nx.eulerian_circuit(multiGraph, source = 0))

    tour = [0]
    for i,j in initial_tour:
        if j not in tour:
            tour.append(j)

    tour_edges = []


    for i in range(len(completeGraph.nodes)):
        tour_edges.append((tour[i-1],tour[i]))



    #nx.draw(G.edge_subgraph(tour_edges), pos=positions)

    #plt.show()

    overall_weight = 0

    for i,j in tour_edges:

        overall_weight += completeGraph.edges[i,j]['length']



    end_time = time.perf_counter()
    run_time = end_time - start_time
    return overall_weight



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



