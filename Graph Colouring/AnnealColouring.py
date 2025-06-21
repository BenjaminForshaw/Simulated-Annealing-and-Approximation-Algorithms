import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import math
import random

def annealColour(edgeList,pointNum):

    e = 2.718
    temperature = 100
    current_solution = []
    for i in range(pointNum):
        current_solution.append(0 + i)
    current_colours = current_solution


    done = False
    while not done:

        neighbouring_solution = current_solution
        node_picked = False
        reps = 0

        while not node_picked:


            allowed_colours = current_colours.copy()
            current_node = random.randint(0,len(current_solution)-1)
            remove_val = current_solution[current_node]

            allowed_colours.remove(remove_val)

            for x in range(len(edgeList)):

                if edgeList[x][0] == current_node:

                    if current_solution[edgeList[x][1]] in allowed_colours:
                        remove_val = current_solution[edgeList[x][1]]
                        allowed_colours.remove(remove_val)
                elif edgeList[x][1] == current_node:
                    if current_solution[edgeList[x][0]] in allowed_colours:
                        remove_val = current_solution[edgeList[x][0]]
                        allowed_colours.remove(remove_val)


            if len(allowed_colours) > 0:
                node_picked = True

        neighbouring_solution[current_node] = random.choice(allowed_colours)

        current_colours = []
        neighbouring_colours = []
        for colour in current_solution:
            if colour not in current_colours:
                current_colours.append(colour)

        for colour in neighbouring_solution:
            if colour not in neighbouring_colours:
                neighbouring_colours.append(colour)



        if len(neighbouring_colours) < len(current_colours):
            current_solution = neighbouring_solution.copy()
            current_colours = neighbouring_colours.copy()

        else:
            probability = e ** ((len(current_colours) - len(neighbouring_colours)) / temperature)

            probcheck = np.random.uniform(0, 1)

            if probcheck <= probability:
                current_solution = neighbouring_solution.copy()
                current_colours = neighbouring_colours.copy()



        temperature = temperature - (0.0005 * temperature/50)




        if temperature <= 1:
            done = True


    return len(current_colours)



def create_graph_colour_graph(num_nodes, edge_prob):
    G = nx.erdos_renyi_graph(num_nodes, edge_prob)  # Creates a random Erdős–Rényi graph
    return G


points = 100
graph = create_graph_colour_graph(points, 0.4)
edges = graph.edges()
edges = list(edges)
  # View the edges of the generated graph




