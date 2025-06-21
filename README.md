# Simulated Annealing and Approximation Algorithms designed for NP-hard problems




In this repository there are 5 folders, each one pertaining to a different NP-hard problem

Each folder contains:

- A python file containing an implemented approximation algorithm
- A python file containing an implemented simulated annealing implementation
- A python file used to compare the findings of the two algorithms


If you wish to test the algorithms, I have entered parameters on each file to allow testing of medium sized graphs of medium density.
These parameters are changeable by altering the values of the "points" and "density" variables respectively.

When using the 'comparison' file, these algorithms are ran 100 times and then notable data is outputted.
These parameters are changeable by altering the value of the 'repetitions' variable.

The aim of designing and implementing these Simulated Annealing Algorithms is to investigate if there are circumstances where Simulated Annealing can outperform Approximation Algorithms.


## The approximation algorithms implemented for NP-hard problems:

- **Maximum Cut** - Goemans-Williamson Algorithm

- **Maximum Independent Set** - Greedy Algorithm

- **Subset Sum Problem** - RGLI Algorithm

- **Graph Colouring** - Greed Algorithm

- **Travelling Salesperson** - Christofides Algorithm
