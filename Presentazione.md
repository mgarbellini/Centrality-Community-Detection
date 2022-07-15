
Title: Finding and evaluating community structure in networks

# # # # # **INTRODUCTION**
#
# % % Slide 01: Outline
#
# % % Slide 02: Motivation
#
# % % Slide 03: Introduction to networks (1)
#
# % % Slide 04: Introduction to networks (2)
#
# # # # # **COMMUNITIES**
#
# % % Slide 05: What is a community? (1)
No definition is universally accepted and usually depends on the specific system at hand.
We can however give an intuitive notion of community namely there must be more edges "inside" the community than edges linking vertices of such community to the rest of the graph.

Additionally, communities tend to be algorithmically defined, i.e. the final product of the
algorithm, without an a priori definition.

# % % Slide 06: What is a community? (2) General required properties
We consider the following as required properties for a community:
    (-) intra-cluster density larger than average link density
    (-) inter-cluster density larger than average link density
    (-) connectedness, must be a path between all vertices in a community C
        that only pass through community C

# % % Slide 07: What is a community? (3) Local, global and vertex similarity definitions
Generally speaking communities are parts of the graph with a few ties with the rest of the graph.

*Local definitions* focus on the subgraph under study, including possibly its immediate neighborhood, but neglecting the rest of the graph.

It is natural to assume that communities are groups of vertices similar to each other. One can then compute the *(vertex) similarity* between each pair of vertices with respect to some reference properties, regardless whether there is an edge connecting them. Each vertex ends up in the cluster whose vertices are the most similar to it. Possible measures of similarity are based on distance definitions (whenever it is possible to define a metric)

Communities can also be defined with respect to the graph as a whole (*global definitions*). This is reasonable in those cases in which clusters are essential parts of the graph, which cannot be taken apart without seriously affecting the functioning of the system.
Although there are mainly indirect definition, some proper definition rely on shedding light on the difference between a random graph and a graph with a possible community structure. For example, a random graph a la Erdos-Renyi is not expected to have a community structure, as any two vertices have the same
probability to be adjacent, so there would be no preferential linking involving specific group of vertices.
One can thus define a null model, i.e. a graph which matches the original in some of its structural features, but which is otherwise a random graph. The null model is then used as a term of comparison, to verify whether the graph at study displays community structure.


# % % Slide 08: How to measure a community? (1) General problem

A community detection algorithm will produce a partition of the input graph, namely a division of a graph in clusters/communities. Generally, partitions can be hierarchically ordered when the graph has different levels of organization at differente scales (can thus be represented as a dendrogram).

A reliable algorithm is supposed to identify good partitions. But what is a good clustering? It is usually necessary to have a quantitative criterion to assess the goodness of a graph partition. This can be done with a quality function that assigns a score to a given graph partition; one defines the best partition as the one with the highest score

# % % Slide 09: How to measure a community? (2) Modularity

The most popular quality function is the modularity of Newman and Girvan. (Ref?).
It is based on the idea that a random graph is not expected to have a cluster structure, so the possible existence of clusters is revealed by the comparison between the actual density of edges in the subgraph and the density one would have expected to have in the subgraph if the graph didn't have any community structure. This expected edge density depends on the chosen null model.
Q = definition
The standard null model of modularity imposes that the expected degree sequence matches the actual degree sequence of the graph.
Properties of modularity:
 - modularity of whole graph is zero
 - max of modularity is one, can be negative [-1/2, 1]

Modularity has thus been used in many algorithm, from a tool to assessing the goodness of the partitions to a optimization quantity for certain algorithms

# % % Slide 10: How to find communities? (1) Overview of methods
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


# % % Slide 11: How to find communities? (2) Divisive algorithms
A simple way to identify communities in a graph is to detect the edges that connect vertices of different communities and remove them, so that the clusters get disconnected from each other.

The crucial point is to find a properties of inter-community edges that could allow for their identification.

Divisive methods do not introduce substantial conceptual advantages with respect to traditional techniques, as they just perform hierarchical clustering on the graph. The only difference is that one removes inter-cluster edges instead of edges with low similarity, and there is no guarantee a priori that inter-cluster edges connect vertices with a low similarity.

The algorithm of Girvan-Newmann which is the topic of the talk falls under this category.

# # # # # **ALGORITHM: Girvan-Newman Community Detection**

# % % Slide 12: Girvan-Newman Algorithm
The Girvan-Newman algorithm is the most popular algorithm for community detection, and it is also historically important since it marked a new era in the field.

The GN algorithm is a divisive algorithm where edges are selected according to the value of measures of *edge centrality*. Edge centrality represents how central and important is an edge in the graph.

The algorithm has the following steps
(-) Computation of centrality for all edges
(-) Remove the edge with largest centrality
(-) Recalculation of centrality on the running graph
(-) Iteration of the cycle from step 2

In particular GN focused on the concept of betweenness (centrality), a variable expressing the frequency of the participation of edges in a particular process. The most used one, within three of the one proposed by GN is edge betweenness centrality, or edge-betweenness for short

# % % Slide 13: Edge betweenness centrality
Edge betweenness is the number of shortest paths between all vertex pairs that run along an edge. It expresses the important of edges in process like information spreading, where information usually flows through shortest paths

If two communities are joined by only a few inter-communities edges, then all paths through the network from vertices in one communities to vertices in the other must pass along on of those few edges. Given a suitable set of paths, one can count how many go along each edge in the graph, and this number we then to be expect to be the largest for the inter-community edges, thus providing a method for identifying them.


Let us note that the recalculation step is the most important feature of the algorithm, since the network without the most between edge is now a different network with a different structure.


# % % Slide 14: Shortest path with BFS
The shortest paths can be found using a breadth-first search.
What is breadth-first search?
Is an algorithm for searching a tree data structure for a node that satisfies a given property. It starts at the tree root and explores all nodes at the present depth prior to moving on to the nodes at the next depth level.
It requires a queue to keep track of the child nodes that were encountered but not yet explored.

# % % Slide 15: Shortest path - Simple case
The simple case serves to illustrate the basic principle of the algorithm.

When there is only a single shortest path from source to any vertex the resulting set of paths forms a shortest-path tree.
We can now use this tree to calculate the contribution to betweenness for each edge from this set of paths as follows. We find first the “leaves” of the tree, i.e., those nodes such that no shortest paths to other nodes pass through them, and we assign a score of 1 to the single edge that connects each to the rest of the tree, as shown in the figure. Then, starting with those edges that are farthest from the source vertex on the tree, i.e., lowest in Fig. 4a, we work upwards, assigning a score to each edge that is 1 plus the sum of the scores on the neighboring edges immediately below it. When we have gone though all edges in the tree, the resulting scores are the betweenness counts for the paths from vertex s. Repeating the process for all possible vertices s and summing the scores, we arrive at the full betweenness scores for shortest paths between all pairs.

# % % Slide 16: Shortest path - Generalization
If multiple shortest paths exist between a pair of vertices they are given equal weights summing to 1 -- e.g. three shortest path are given weight 1/3.
To calculate correctly what fraction of the paths flow along each edge in the network, we generalize the breadth-first search part of the calculation, as follows

(1) The initial vertex s is given distance ds = 0 and a weight ws = 1
(2) Every vertex i adjacent to s is given distance di = ds + 1 = 1, and weight wi = ws = 1.
(3) For each vertex j adjacent to one of those vertices i we do one of three things:
(3a) If j has not yet been assigned a distance, it is assigned distance dj = di + 1 and weight wj = wi.
(3b) If j has already been assigned a distance and dj = di + 1, then the vertex’s weight is increased by wi, that is wj ← wj + wi.
(3c) If j has already been assigned a distance and dj < di + 1, we do nothing.
(4) Repeat from step 3 until no vertices remain that have assigned distances b


# % % Slide 17: Betweenness - Accumulation
Physically, the weight on a vertex i represents the number of distinct paths from the source vertex to i.
These weights are precisely what we need to calculate our edge betweennesses, because if two vertices i and j are connected, with j farther than i from the source s, then the fraction of a geodesic path from j through i to s is given by wi/wj. Thus, to calculate the contribution to edge betweenness from all shortest paths starting at s, we need only carry out the following steps:

(1) Find every “leaf” vertex t, i.e., a vertex such that no paths from s to other vertices go though t.
(2) For each vertex i neighboring t assign a score to the edge from t to i of wi/wt.
(3) Now, starting with the edges that are farthest from the source vertex s—lower down in a diagram such as Fig. 4b—work up towards s. To the edge from vertex i to vertex j, with j being farther from s than i, assign a score that is 1 plus the sum of the scores on the neighboring edges immediately below it (i.e., those with which it shares a common vertex), all multiplied by wi/wj.
(4) Repeat from step 3 until vertex s is reached.

# % % Slide 18: Pseudo-code (1) Shortest path
Recap and comment on pseudocode. This should allow the time to explain all the data structures used, namely queues and stacks -- together with the list of predecessor necessary for the accumulation part

# % % Slide 19: Pseudo-code (2) Accumulation and Betweenness
Recap and comment on pseudocode. This should allow the time to explain all the data structures used, namely queues and stacks -- together with the list of predecessor necessary for the accumulation part

# % % Slide 20: Edge removal and new partition
Once the most between edge has been found -- if multiples are found one is chosen at random -- it is removed from the original graph. This results in a new graph with possible new partitions (not necessarily the most between edge is the only one connecting two communities).

The new graph is stored and the process is repeated until no more edges are present in the graph, i.e. each vertex is itself a community.

# % % Slide 21: Final result: dendrogram
The final result can be displayed through a dendrogram where partition are found by looking at connected components (via BFS). To determine the result of the algorithm, namely which is the best community structure, it is necessary to compute the modularity at each level of the dendrogram. The highest value of modularity represents the solution. One can also decide at which scale consider the community structure. If multiple values are present, it depends on the scope of the research.

# # # # # ALGORITHM ANALYSIS
#
# % % Slide 22: Notes on assessing correctness

Assessing the correctness of the GN algorithm is a tricky task

(1) Communities are not really well defined. Thus we're not looking for something whose form is quell known. The so called 'correct output' does not exist and as mentioned before the chosen solution depends on the scope of the study

(2) The process of finding the solution to the community detection problem only happens after the iterative partition of the graph, thus one cannot apply any loop invariant properties of the algorithm.

Therefore we can do the following

(1) Show that the core algorithmic feature -- the shortest path -- is indeed correct
(2) Run the algorithm on synthetic networks or real networks whose community structure is known a priori. In this manner one can compare the fraction of nodes correctly identified in each community.


# % % Slide 23: Shortest path (BFS) correctness



# % % Slide 24: Benchmark with synthetic network

The following is from Girvan-Newman.
We have generated a large number of graphs with n=128 divided into four communities of 32 vertices each. Edges are placed independently at random between vertex pairs with probability pin for an edge to fall between vertices in the same community and pout to fall between vertices in different communities. The values of pin and pout were chosen to make the expected degree of each vertex equal to 16.

The result can be seen in terms of the maximum value of modularity corresponding to the division into four expected communities and in the plot showing the fraction of vertices classified correctly as a function of the mean number of vertices .... (continues on paper)

# % % Slide 25: Time complexity of the algorithm
#
# % % Slide 26: Space complexity (?)
#
# # # # # CODE and IRL BENCHMARKS
#
# % % Slide 27: Famous and interesting networks
#
# % % Slide 28: Validating time complexity
#
# % % Slide 29: Algorithm implementation
