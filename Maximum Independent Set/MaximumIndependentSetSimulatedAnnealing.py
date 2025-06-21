import random
import numpy as np
import networkx as nx
import time
def maximumIndependentAnnealing(graph, pointAmount):
    start_time = time.perf_counter()
    random.shuffle(graph)
    pointLabels = []

    '''Each graph point is given a label'''
    for i in range(pointAmount):
        pointLabels.append(0)

    startingNode = random.randint(0, len(pointLabels) - 1)

    pointLabels[startingNode] = 1


    '''
    Starting node in independent set is randomly allocated and adjacent nodes are labelled
    '''
    for i in range(len(graph)):
        if graph[i][0] == startingNode:
            pointLabels[graph[i][1]] = 0
        elif graph[i][1] == startingNode:
            pointLabels[graph[i][0]] = 0



    done = False
    temperature = 100
    e = 2.718


    while not done:

        '''
        Independent set is a list of all nodes in the independent set
        '''

        independentSet = []
        nonIndependentSet = []
        for i in range(len(pointLabels)):
            if pointLabels[i] == 1:
                independentSet.append(i)
            else:
                nonIndependentSet.append(i)



        '''Random node from the independent set is selected'''
        randomSelection = random.randint(0,len(independentSet)-1)
        currentNode = independentSet[randomSelection]



        '''Random node not in the independent set is selected'''
        randomSwap = random.randint(0,len(nonIndependentSet)-1)
        currentSwap = nonIndependentSet[randomSwap]


        pointLabels[currentNode] = 0
        pointLabels[currentSwap] = 1


        '''
        If the swap is valid, check the degree of each node.
        '''

        if verifyValidGraph(graph, pointLabels):
            currentDegreeCount = 0
            swapDegreeCount = 0

            for x in range(len(graph)):

                if (graph[x][0] == currentSwap):
                    swapDegreeCount += 1

                elif (graph[x][1] == currentSwap):
                    swapDegreeCount += 1

                elif (graph[x][0] == currentNode):
                    currentDegreeCount += 1

                elif (graph[x][1] == currentNode):
                    currentDegreeCount += 1


            if currentDegreeCount >= swapDegreeCount:

                for i in range(len(pointLabels)):
                    if pointLabels[i] != 1:

                        pointLabels[i] = 1
                        validGraph = verifyValidGraph(graph, pointLabels)
                        if validGraph == False:

                            pointLabels[i] = 0


            else:

                probability = e ** ((currentDegreeCount-swapDegreeCount) / temperature)
                probcheck = np.random.uniform(0, 1)

                if probcheck > probability:
                    pointLabels[currentNode] = 1
                    pointLabels[currentSwap] = 0
                else:
                    for i in range(len(pointLabels)):
                        if pointLabels[i] != 1:

                            pointLabels[i] = 1
                            validGraph = verifyValidGraph(graph, pointLabels)
                            if validGraph == False:
                                pointLabels[i] = 0


        else:
            pointLabels[currentNode] = 1
            pointLabels[currentSwap] = 0



        temperature = temperature - (0.0005 * temperature/50)

        if temperature <=1:
            done = True


    independentCount = 0
    for i in range(len(pointLabels)):
        if pointLabels[i] == 1:
            independentCount += 1
    end_time = time.perf_counter()
    runtime = end_time - start_time

    return independentCount





def verifyValidGraph(graph, pointLabels):

    valid = True
    '''
    1. For each node that is in the independent set;
    2. Look through the graph to see if there is no conflicts
    3. A conflict would be where there is an edge between two nodes in the independent set
    
    '''

    for j in range(len(graph)):
        if pointLabels[graph[j][0]] == 1:
            if pointLabels[graph[j][1]] == 1:
                valid = False

    return valid



def create_max_cut_graph(num_nodes, edge_prob):

    G = nx.erdos_renyi_graph(num_nodes, edge_prob)  # Creates a random Erdős–Rényi graph

    return G


