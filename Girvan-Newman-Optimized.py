"""
@author:    M. Garbellini
@email:     matteo.garbellini@studenti.unimi.it
@course-project: Algoritmi e Strutture Dati, Università degli Studi di Milano

Girvan-Newman algorithm for community detection in networks
"""
from collections import deque
import random
import time
import numpy as np
import logging
import sys


import numpy as np
from numba import njit
from numba import int32, int64, float64
from numba import types, typed, typeof, deferred_type
from numba.experimental import jitclass


def girvan_newman_community_detection(G):


    # assess the graph before running the algorithm
    G.connected_components()
    community_structure = [G.community_structure]
    number_of_communities = [G.num_components]
    max_modularity = compute_modularity(G)
    solution_num_communities = number_of_communities

    iter = 0
    # until we get single node community
    while len(G.get_edges()) > 0:

        iter+= 1

        # computes betweenness for the graph
        betweenness = edge_betweenness_centrality(G)

        # find most valuable/between edge
        edge_to_be_removed = most_between_edge(betweenness)

        # remove most between edge
        G.remove_edge(edge_to_be_removed[0], edge_to_be_removed[1])

        # find new modularity
        modularity = compute_modularity(G)

        # add new partition dictionary to communities list
        G.connected_components()
        community_structure.append(G.community_structure)
        number_of_communities.append(G.num_components)

        # save if improvement
        if modularity > max_modularity:
            max_modularity = modularity
            solution_num_communities = G.num_components


    # printing final solution
    print('Modularity: ', max_modularity, ' - # Communities: ', solution_num_communities)


def edge_betweenness_centrality(G):
    """Computes the edge betweenness centrality by running modified shortest
    path algorithm."""
    betweenness = dict.fromkeys(G.get_edges(), 0.0)

    for node in G:
        # use BFS for shortest path from source s to all other nodes
        S, P, sigma = shortest_path_bfs(G, node)

        # accumulate betweenness for all edges
        betweenness = accumulate_betweenness(betweenness, S, P, sigma, node)

    # normalize betweenness for undirected graphs
    for edge in betweenness:
        betweenness[edge] *= 0.5

    #return betweenness
    return betweenness


def accumulate_betweenness(betweenness, S, P, sigma, s):
    """Accumulates the edge betweenness for all the nodes"""
    delta = dict.fromkeys(S, 0)
    while S:
        w = S.pop()
        coeff = (1 + delta[w]) / sigma[w]
        for v in P[w]:
            c = sigma[v] * coeff
            betweenness[(w, v)] += c
            betweenness[(v, w)] += c
            delta[v] += c
    return betweenness


def shortest_path_bfs(G, s):
    S = []
    P = {}
    for v in G:
        P[v] = []
    sigma = dict.fromkeys(G, 0.0)  # sigma[v]=0 for v in G
    D = {}
    sigma[s] = 1.0
    D[s] = 0
    Q = deque([s])
    while Q:  # use BFS to find shortest paths
        v = Q.popleft()
        S.append(v)
        Dv = D[v]
        sigmav = sigma[v]
        for w in G[v]:
            if w not in D:
                Q.append(w)
                D[w] = Dv + 1
            if D[w] == Dv + 1:  # this is a shortest path, count paths
                sigma[w] += sigmav
                P[w].append(v)  # predecessors
    return S, P, sigma


def most_between_edge(betweenness):

    mx = max(betweenness.values())
    max_keys = [k for k, v in betweenness.items() if v == mx]
    if len(max_keys) > 2:
        between_edge = random.choice(max_keys)
    else:
        between_edge = max_keys[0]

    return between_edge


def compute_modularity(G):
    Q = 0
    m = float(np.sum(G.adj_matrix))/2
    k = np.sum(G.adj_matrix, axis = 0)
    for i in range(len(G.adj_matrix[0])):
        for j in range(len(G.adj_matrix[0])):

            # only if both vertices belong to same community
            if G.community_structure[i+1] == G.community_structure[j+1]:
                Q += G.adj_matrix[i][j] - k[i]*k[j]/m/2

    return np.round(Q/m/2, 7)

@njit
def empty_list():
    l = [int64(10)]
    l.clear()
    return l


specnode =[
    ('neighbor', types.List(int64)),
    ('id', int64),
    ]
@jitclass(specnode)
class Node:
    """Node class containing list of neighbors"""
    def __init__(self, id):
        self.id = id
        self.neighbor = empty_list()
"""
specgraph = [
    ('n', int32),
    ('m', int32),
    ('node', types.ListType((Node.class_type.instance_type)),
    ]

@jitclass(specgraph)
class Graph:
"""
if __name__ == '__main__':


    nodo1 = Node(1)
    neighbors = typed.List(int64)
    neighbors.append(3)
    nodo1.neighbor= neighbors
    print(nodo1.neighbor)
