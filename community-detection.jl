#=
@author:    M. Garbellini
@email:     matteo.garbellini@studenti.unimi.it
@course-project: Algoritmi e Strutture Dati, Università degli Studi di Milano

GREEDY COMMUNITY DETECTION in networks

**Objective**
It has been found that many networks display community structure—groups of vertices
within which connections are dense but between which they are sparser—and highly
sensitive computer algorithms have in recent years been developed for detecting
such structure. These algorithms however are computationally demanding, which limits
their application to small networks [1].

The goal is to implement Newman algorithm which improves on previous algorithms and
allows the study of larger networks -- with time complexity of O(nm^2)[1]. We then
implement the Clauset-Newman-Moore algorithm which, by using an improved data structure
and some ingenious calculation of modularity, is able to achieve a time complexity
of O(nmlogm) [2].

[1] Newman, M.E.J., 2004. Fast algorithm for detecting community structure in networks.
    Phys. Rev. E 69, 066133. https://doi.org/10.1103/PhysRevE.69.066133

[2] Clauset, A., Newman, M.E.J., Moore, C., 2004. Finding community structure in very
    large networks. Phys. Rev. E 70, 066111. https://doi.org/10.1103/PhysRevE.70.066111

**Newman Algorithm**
The algorithm consists in a greedy optimization of the modularity, a quality function that
describes how meaningful is a given community division. The algorithm is given by the
following steps:

    1. Each node is set to a different community (thus at this point we have n communities)
    2. Pairs of community are repeatedly joined by choosing the greatest increase (or smaller
        decrease) of modularity.
    3. The algorithm stops when there is only one community left and a dendogram is produced
    4. By cutting through the dendogram we can choose the level at which the division produced
        an overall maximum of modularity

**Clauset-Newman-Moore Algorithm**



Latest update: May 18th 2022
=#
