import random
import time

import matplotlib.pyplot as plt
import numpy as np
from MaximumCutCalc import maxCut
import networkx as nx

def simulatedAnnealingMaximumCut(edges, points):
    start_time = time.perf_counter()
    pointValues = []
    ''' Initial random allocation of points to either group. Subject to change. '''
    for i in range(points):

        coinflip = np.random.uniform(-1, 1)

        if coinflip > 0:
            pointValues.append(1)
        else:
            pointValues.append(-1)


    currentResult = maxCut(edges, pointValues)

    ''' 
    1. We clone the point values so we can flip them to create neighbouring solutions.
    2. Improvement Loop is our neighbouring solution comparison algorithmn
    3, Current flip is the index of the current point we are flipping to the other group
    4. Neighbour Value is the maxCut of the current neighbout we are assessing
    5. Current 'temperature' of algorithmn
    6. The constant 'e'
    7. The probability we accept a neighbour which doesn't improve the solution
    '''
    clonedValues = pointValues
    improvementLoop = True
    currentFlip = 0
    neighbourValue = 0
    temperature = 100
    e = 2.718
    probability = 0



    ''' While the improvement loop runs, one point value is flipped at a time. 
    
    If it is an improvement, it becomes the current best result, the neighbouring graph allocation
    becomes the current allocation and the loop resets.
        
    If it isn't an improvement, then the graph point values are reset and the index of the flip increases, meaning
    we will flip a different point next time round.
        
    NOTE: this isn't fully fleshed out Simulated Annealing yet. Need to figure out temperature equation properly
    It also might be the case that you take the best swap out of all neighbours of the current solution, not just
    the first one you come across.
    
    
    '''
    while improvementLoop == True:

        currentFlip = random.randint(0,len(clonedValues)-1)

        clonedValues[currentFlip] = clonedValues[currentFlip] * -1

        neighbourValue = maxCut(edges, clonedValues)

        if neighbourValue >= currentResult:

            currentResult = neighbourValue
            pointValues = clonedValues

        else:

            probability = e ** ((neighbourValue - currentResult) / temperature)

            probcheck = np.random.uniform(0,1)

            if probcheck <= probability:
                currentResult = neighbourValue
                pointValues = clonedValues

            else:

                clonedValues = pointValues


        temperature = temperature - (0.5 * temperature / 50)


        if temperature <= 1:
            improvementLoop = False


    end_time = time.perf_counter()
    run_time = end_time - start_time
    print("SA run time: ",run_time)
    return currentResult




def create_max_cut_graph(num_nodes, edge_prob):

    G = nx.erdos_renyi_graph(num_nodes, edge_prob)  # Creates a random Erdős–Rényi graph

    return G


''' Amount of points in the graph. '''
points = 100
graph = create_max_cut_graph(points, 0.6)
edges = graph.edges()
edges = list(edges)
  # View the edges of the generated graph











