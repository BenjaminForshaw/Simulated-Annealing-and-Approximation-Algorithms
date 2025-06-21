def maxCut(edge, points):
    '''Max cut calculation is performed and result is outputted.'''
    maximumCut = 0
    for i in range(len(edge)):
        currentEdge = 1 - (points[edge[i][0]] * points[edge[i][1]])
        currentEdge = currentEdge/2

        maximumCut += currentEdge


    return maximumCut
