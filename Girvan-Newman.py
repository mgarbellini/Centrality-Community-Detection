"""
@author:    M. Garbellini
@email:     matteo.garbellini@studenti.unimi.it
@course-project: Algoritmi e Strutture Dati, Università degli Studi di Milano

Girvan-Newman algorithm for community detection in networks
"""
from collections import deque

class Graph:
    """Graph class based on adjacency list implemented with dictionaries"""

    def __init__(self):
        self.adj_list = {}
        self.community_structure = {}
        self.num_components = None

    def __iter__(self):
        return iter(self.adj_list.keys())

    def __getitem__(self, n):
        return self.adj_list[n]

    def load_adj_list(self, adj_list):
        self.adj_list = adj_list
        self.community_structure = dict.fromkeys(self.adj_list, 0)

    def add_edge(self, v, w):
        if v not in self.adj_list:
            self.community_strucuture.update({v: 0})
            self.adj_list.update({v:[w]})
            if w not in self.adj_list:
                self.adj_list.update({w:[v]})
            else:
                self.adj_list[w].append(v)
        elif w not in self.adj_list:
            self.community_structure.update({w: 0})
            self.adj_list[v].append(w)
            self.adj_list.update({w:[v]})
        else:
            self.adj_list[v].append(w)
            self.adj_list[w].append(v)

    def remove_edge(self, v, w):
        del self.adj_list[v][self.adj_list[v].index(w)]
        del self.adj_list[w][self.adj_list[w].index(v)]

    def connected_components(self):
        seen = set()
        component = 0
        for node in self.adj_list:
            if node not in seen:
                component += 1
                Q = deque([node])
                while Q:
                    v = Q.popleft()
                    self.community_structure[v] = component
                    seen.add(v)
                    for w in self.adj_list[v]:
                        if w not in seen:
                            Q.append(w)

        self.num_components = component

def girvan_newman_community_detection():


    mx = max(betweenness.values())
    max_keys = [k for k, v in betweenness.items() if v == mx]
    if len(max_keys) > 2:
        most_between_edge = random.choice(max_keys)
    else:
        most_between_edge = max_keys[0]

    return

def edge_betweenness_centrality(G):
    """Computes the edge betweenness centrality by running modified a shortest
    path algorithm."""

    betweenness = dict.fromkeys(G.get_edges, 0.0)

    for node in G:
        # use BFS for shortest path from source s to all other nodes
        S, P, sigma = shortest_path_bfs(G, node)

        # accumulate betweenness for all edges
        betweenness = accumulate_betweenness(betweenness, S, P, sigma, node)

    # normalize betweenness for undirected graphs
    betwenness *= 0.5

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
            if (v, w) not in betweenness:
                betweenness[(w, v)] += c
            else:
                betweenness[(v, w)] += c
            delta[v] += c
        if w != s:
            betweenness[w] += delta[w]
    return betweenness



"""edge betweenness function"""
def _edge_betweenness_centrality(G, k=None, normalized=True):






def _single_source_shortest_path_basic(G, s):
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
    return S, P, sigma, D
