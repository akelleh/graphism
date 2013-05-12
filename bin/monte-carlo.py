#!/usr/bin/env python

from graphism import graph as g
import numpy

NODES = 1000
PERIOD = 75
infection_curves = []
SEEDS = 100

for iteration in range(30):
    infected = []
    edges = []
    seed_nodes = []
    
    print "Building edge list..."
    for i in range(NODES):
        for j in range(NODES):
            if i != j:
                edges.append((i,j))
    
    print "Adding edges to graph..."
    graph = g.Graph(edges)    
    
    graph.infect_seeds([graph.get_node_by_name(n) for n in range(SEEDS)])
    
    print "Propagating infection..."
    for t in range(PERIOD):
        graph.propagate()
        infected.append(len(graph.infected()))
        
    infection_curves.append(infected)

print [numpy.mean(tup) for tup in zip(*infection_curves)]
