import random
import networkx as nx
import matplotlib.pyplot as plt
import math
import numpy as np
def annealAlg(G, positions):

    current_solution = list(G.nodes)
    random.shuffle(current_solution)
    current_solution_weight = weightCalculation(current_solution,G)
    e = 2.718
    temperature = 100



    done = False

    while not done:


        randomsFound = False

        while not randomsFound:
            random1 = random.choice(current_solution)
            random2 = random.choice(current_solution)
            if random1 != random2:
                randomsFound = True


        neighbouringSolution = current_solution
        for i in range(len(neighbouringSolution)):
            if neighbouringSolution[i] == random1:
                neighbouringSolution[i] = random2
            elif neighbouringSolution[i] == random2:
                neighbouringSolution[i] = random1


        neighbouring_solution_weight = weightCalculation(neighbouringSolution,G)


        if neighbouring_solution_weight < current_solution_weight:
            current_solution = neighbouringSolution
            current_solution_weight = neighbouring_solution_weight

        else:
            probability = e ** ((current_solution_weight-neighbouring_solution_weight) / temperature)
            probcheck = np.random.uniform(0, 1)

            if probcheck <= probability:
                current_solution = neighbouringSolution
                current_solution_weight = neighbouring_solution_weight


        temperature = temperature - (0.0005 * temperature/50)



        if temperature <= 1:
            done = True












    return current_solution_weight



def weightCalculation(solution,graph):
    current_weight = 0
    for i in range(len(solution)-1):
        current_weight += graph.edges[solution[i],solution[i+1]]['length']

    current_weight += graph.edges[solution[len(solution)-1],solution[0]]['length']

    return current_weight






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






