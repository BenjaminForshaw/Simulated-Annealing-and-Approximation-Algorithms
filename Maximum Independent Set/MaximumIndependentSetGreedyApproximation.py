import networkx as nx
import time
'''Greedy Approximation Algorithmn'''
def greedyApproximation(graph,pointAmount):
    start_time = time.perf_counter()
    pointLabels = []

    '''Each graph point is given a label'''
    for i in range(pointAmount):
        pointLabels.append(2)


    done = False

    while done == False:
        smallestDegree = 999999
        currentChoice = 0

        '''
        For each graph point;
        1. Look through the list of unlabelled edges
        2. If there is an edge that involves the current graph point, and the other
         point involved is unlabelled, add 1 to the degree count
        3. When all edges have been checked, if the degree is smaller than smallestDegree then
        replace it and establish the current point with the smallest degree count
        
        '''
        for i in range(len(pointLabels)):

            degreeCount = 0

            if pointLabels[i] == 1 or pointLabels[i] == 0:
                degreeCount = smallestDegree + 1

            else:

                for x in range(len(graph)):

                    if (graph[x][0] == i):
                        if pointLabels[graph[x][1]] == 2:
                            degreeCount += 1

                    if (graph[x][1] == i):
                        if pointLabels[graph[x][0]] == 2:
                            degreeCount += 1



            if degreeCount < smallestDegree:
                smallestDegree = degreeCount
                currentChoice = i



        '''
        1. The current lowest degree node is labelled as 1
        2. We look through the list of edges, and if any of the edges involve the current choice,
        we label the other node involved as 0.
        '''
        pointLabels[currentChoice] = 1
        for i in range(len(graph)):
            if graph[i][0] == currentChoice:
                pointLabels[graph[i][1]] = 0
            elif graph[i][1] == currentChoice:
                pointLabels[graph[i][0]] = 0


        done = True
        for i in range(len(pointLabels)):
            if pointLabels[i] == 2:
                done = False


    finalCount = 0
    for i in range(len(pointLabels)):
        if pointLabels[i] == 1:
            finalCount += 1

    end_time = time.perf_counter()
    runTime = end_time - start_time

    return finalCount









def create_max_cut_graph(num_nodes, edge_prob):

    G = nx.erdos_renyi_graph(num_nodes, edge_prob)  # Creates a random Erdős–Rényi graph

    return G



points = 100
graph = create_max_cut_graph(points, 0.4)
edges = graph.edges()
edges = list(edges)
