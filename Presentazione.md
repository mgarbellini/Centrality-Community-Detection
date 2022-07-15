
Title: Finding and evaluating community structure in networks

# # # # # **INTRODUCTION**
#
# % % Slide 01: Outline
#
# % % Slide 02: Motivation
#
# % % Slide 03: Introduction to networks
#
# # # # # **COMMUNITIES**
#
# % % Slide 04: What is a community? (1)
No definition is universally accepted and usually depends on the specific system at hand.
We can however give an intuitive notion of community namely there must be more edges "inside" the community than edges linking vertices of such community to the rest of the graph.

Additionally, communities tend to be algorithmically defined, i.e. the final product of the
algorithm, without an a priori definition.

# % % Slide 05: What is a community? (2) General required properties
We consider the following as required properties for a community:
    (-) intra-cluster density larger than average link density
    (-) inter-cluster density larger than average link density
    (-) connectedness, must be a path between all vertices in a community C
        that only pass through community C

# % % Slide 06: What is a community? (3) Local, global and vertex similarity definitions
Generally speaking communities are parts of the graph with a few ties with the rest of the graph.

*Local definitions* focus on the subgraph under study, including possibly its immediate neighborhood, but neglecting the rest of the graph.

It is natural to assume that communities are groups of vertices similar to each other. One can then compute the *(vertex) similarity* between each pair of vertices with respect to some reference properties, regardless whether there is an edge connecting them. Each vertex ends up in the cluster whose vertices are the most similar to it. Possible measures of similarity are based on distance definitions (whenever it is possible to define a metric)

Communities can also be defined with respect to the graph as a whole (*global definitions*). This is reasonable in those cases in which clusters are essential parts of the graph, which cannot be taken apart without seriously affecting the functioning of the system.
Although there are mainly indirect definition, some proper definition rely on shedding light on the difference between a random graph and a graph with a possible community structure. For example, a random graph a la Erdos-Renyi is not expected to have a community structure, as any two vertices have the same
probability to be adjacent, so there would be no preferential linking involving specific group of vertices.
One can thus define a null model, i.e. a graph which matches the original in some of its structural features, but which is otherwise a random graph. The null model is then used as a term of comparison, to verify whether the graph at study displays community structure.


# % % Slide 07: How to measure a community? (1) General problem

A community detection algorithm will produce a partition of the input graph, namely a division of a graph in clusters/communities. Generally, partitions can be hierarchically ordered when the graph has different levels of organization at differente scales (can thus be represented as a dendrogram).

A reliable algorithm is supposed to identify good partitions. But what is a good clustering? It is usually necessary to have a quantitative criterion to assess the goodness of a graph partition. This can be done with a quality function that assigns a score to a given graph partition; one defines the best partition as the one with the highest score

# % % Slide 08: How to measure a community? (2) Modularity

The most popular quality function is the modularity of Newman and Girvan. (Ref?).
It is based on the idea that a random graph is not expected to have a cluster structure, so the possible existence of clusters is revealed by the comparison between the actual density of edges in the subgraph and the density one would have expected to have in the subgraph if the graph didn't have any community structure. This expected edge density depends on the chosen null model.
Q = definition
The standard null model of modularity imposes that the expected degree sequence matches the actual degree sequence of the graph.
Properties of modularity:
 - modularity of whole graph is zero
 - max of modularity is one, can be negative [-1/2, 1]

Modularity has thus been used in many algorithm, from a tool to assessing the goodness of the partitions to a optimization quantity for certain algorithms

# % % Slide 09: How to find communities? (1) Overview of methods
Many different algorithm for community detection exist in literature. We can briefly take a look at them.

*Traditional methods*
 - Graph partitioning: some information on the clustering size and number of cluster is needed
 - Hierarchical clustering: finding multilevel (hierarchical) structure of the graph using similarity measures (based on vertex similarity). Can usually be divided in agglomerative (bottom up) and divisive algorithms (top down).
 Disadvantages of agglomerative algorithms?

*Divisive algorithm*
 - Algorithm of Girvan and Newman, based on edge betweenness

*Modularity-based methods*
 - Modularity optimization
 - General heuristic methods


# % % Slide 10: How to find communities? (2) Divisive algorithms
A simple way to identify communities in a graph is to detect the edges that connect vertices of different communities and remove them, so that the clusters get disconnected from each other.

The crucial point is to find a properties of inter-community edges that could allow for their identification.

Divisive methods do not introduce substantial conceptual advantages with respect to traditional techniques, as they just perform hierarchical clustering on the graph. The only difference is that one removes inter-cluster edges instead of edges with low similarity, and there is no guarantee a priori that inter-cluster edges connect vertices with a low similarity.

The algorithm of Girvan-Newmann which is the topic of the talk falls under this category.

# # # # # **ALGORITHM: Girvan-Newman Community Detection**

# % % Slide 11: Girvan-Newman Algorithm
The Girvan-Newman algorithm is the most popular algorithm for community detection, and it is also historically important since it marked a new era in the field.

The GN algorithm is a divisive algorithm where edges are selected according to the value of measures of *edge centrality*. Edge centrality represents how central and important is an edge in the graph.

The algorithm has the following steps
(-) Computation of centrality for all edges
(-) Remove the edge with largest centrality
(-) Recalculation of centrality on the running graph
(-) Iteration of the cycle from step 2

In particular GN focused on the concept of betweenness (centrality), a variable expressing the frequency of the partecipation of edges in a particular process. The most used one, whithin three of the one proposed by GN is edge betweenness centrality, or edge-betweenness for short

# % % Slide 11: Edge betweenness centrality
Edge betweenness is the number of shortest paths between all vertex pairs that run along an edge. It expresses the important of edges in process like information spreading, where information usually flows through shortest paths

If two communities are joined by only a few inter-communities edges, then all paths through the network from vertices in one communities to vertices in the other must pass along on of those few edges. Given a suitable set of paths, one can count how many go along each edge in the graph, and this number we then to be expect to be the largest for the inter-community edges, thus providing a method for identifying them.


Let us note that the recalculation step is the most important feature of the algorithm, since the network without the most between edge is now a different network with a different structure.


# % % Slide 12: Shortest path with BFS
The shortest paths can be found using a breadth-first search.
What is breadth-first search?
Is an algorithm for searching a tree data structure for a node that satisfies a given property. It starts at the tree root and explores all nodes at the present depth prior to moving on to the nodes at the next depth level.
It requires a queue to keep track of the child nodes that were encountered but not yet explored.

# % % Slide 13: Shortest path - Simple case
The simple case serves to illustrate the basic principle of the algorithm.

When there is only a single shortest path from source to any vertex the resulting set of paths forms a shortest-path tree.
We can now use this tree to calculate the contribution to betweenness for each edge from this set of paths as follows. We find first the “leaves” of the tree, i.e., those nodes such that no shortest paths to other nodes pass through them, and we assign a score of 1 to the single edge that connects each to the rest of the tree, as shown in the figure. Then, starting with those edges that are farthest from the source vertex on the tree, i.e., lowest in Fig. 4a, we work upwards, assigning a score to each edge that is 1 plus the sum of the scores on the neighboring edges immediately below it. When we have gone though all edges in the tree, the resulting scores are the betweenness counts for the paths from vertex s. Repeating the process for all possible vertices s and summing the scores, we arrive at the full betweenness scores for shortest paths between all pairs.

# % % Slide 14: Shortest path - General case
If multiple shortest paths exist between a pair of vertices they are given equal weights summing to 1 -- e.g. three shortest path are given weight 1/3.
To calculate correctly what fraction of the paths flow along each edge in the network, we generalize the breadth-first search part of the calculation, as follows



# % % Slide 15: Betweenness - Accumulation


# % % Slide 16: Pseudo-code
# % % Slide 12: Edge removal and new partition
#
# % % Slide 13: Final result: dendrogram
# 
# % % Slide 14: Final result: community structure
#
# # # # # ALGORITHM ANALYSIS
#
# % % Slide 15: Notes on assessing correctness
#
# % % Slide 16: Shortest path (BFS) correctness
#
# % % Slide 17: Benchmark with known community structure
#
# % % Slide 18: Time complexity of the algorithm
#
# % % Slide 19: Space complexity (?)
#
# # # # # CODE and IRL BENCHMARKS
#
# % % Slide 20: Famous and interesting networks
#
# % % Slide 21: Validating time complexity
#
# % % Slide 22: Algorithm implementation
