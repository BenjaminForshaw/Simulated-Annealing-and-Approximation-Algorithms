import cvxpy as cp
import numpy as np
from scipy.linalg import sqrtm
from MaximumCutCalc import maxCut
from SimulatedAnnealingImplementation import simulatedAnnealingMaximumCut
from matplotlib import pyplot as plt
import networkx as nx
import time

'''
The process of implementing Goemans & Williamson in python has been aided by 'Goemans-Williamson Max-Cut Algorithm | The Practical Guide to Semidefinite Programming (4/4)' by Visually Explained.
This has also been added as a reference on my dissertation.
'''


''' Goemans & Williamson approximation ratio of 87% 

1. Instead of points having one value (either 1 or -1), they hold a variable that is a vector between 1 and -1,
'scalars'

2. A 'Hyperplane' is put at a random angle between these vectors. Vectors on one side of the plane are one set, and the
ones on the other side are another set.

'''


import cvxpy as cp
def GoemansWilliamsonMaxCut(graph, points):
    start_time = time.perf_counter()
    '''Matrix is established. Has same amount of rows and columns as the amount of points in the graph.'''
    Matrix = cp.Variable((points,points), symmetric=True)

    '''Diagonals of matrix are set to 1 as we want unit vectors. Matrix is positive semidefinite.'''
    restrictions = [Matrix >> 0]
    restrictions += [Matrix[i,i] == 1 for i in range (points)]

    formula = sum(0.5*(1-Matrix[i,j]) for (i,j) in graph)
    problem = cp.Problem(cp.Maximize(formula), restrictions)

    problem.solve()

    '''Matrix is square rooted to provide us with each graph point's vector. 
    A random hyperplane is then generated, separating the graph points into separate groups.'''
    vectorMatrix = sqrtm(Matrix.value)
    hyperplane = np.random.rand(points)
    vectorMatrix = np.sign(vectorMatrix @ hyperplane)


    '''Graph points are then rounded to either positive(1) or negative(-1) in order
    to perform our max cut calculation. '''
    pointVals = []
    for i in vectorMatrix:
        if i > 0:
            pointVals.append(1)
        else:
            pointVals.append(-1)


    result = maxCut(graph, pointVals)
    end_time = time.perf_counter()
    run_time = end_time - start_time


    return result



''' An example graph. Max cut calculated should be 5. '''
edges = [(0,1),
         (0,2),
         (1,3),
         (1,4),
         (2,3),
         (3,4)]

def create_max_cut_graph(num_nodes, edge_prob):

    G = nx.gnp_random_graph(num_nodes, edge_prob)  # Creates a random Erdős–Rényi graph

    return G


''' Amount of points in the graph. '''
points = 100
graph = create_max_cut_graph(points, 0.4)
edges = graph.edges()
edges = list(edges)
  # View the edges of the generated graph

