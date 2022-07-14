"""
Testing an graph implementation using dictionaries """

from collections import deque
import random

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

    def get_edges(self):
        edges = []
        for node in self.adj_list:
            for neighbour in self.adj_list[node]:
                edges.append((node, neighbour))

        return edges


graph = {
        "A" : ["B", "C"],
        "B" : ["C", "A"],
        "C" : ["A", "B", "D"],
        "D" : ["C", "E", "F"],
        "E" : ["D"],
        "F" : ["D", "G"],
        "G" : ["F"]
        }


test = Graph()
test.load_adj_list(graph)
test.remove_edge("D", "F")


#reading test
with open("soc-karate.txt") as file:
    for line in file:
        edge = line.split()
        print(int(edge[0]))

"""
betweenness = dict.fromkeys(test.get_edges(), 0.0)
betweenness[('A', 'B')] = 1.0
betweenness[('B', 'A')] = 1.0
betweenness[('E', 'D')] = 1.1
betweenness[('D', 'E')] = 1.1


mx = max(betweenness.values())
max_keys = [k for k, v in betweenness.items() if v == mx]
if len(max_keys) > 2:
    most_between_edge = random.choice(max_keys)
else:
    most_between_edge = max_keys[0]
"""

#most_between_edge = max(betweenness, key=betweenness.get)
#print(most_between_edge)
