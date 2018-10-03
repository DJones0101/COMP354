# COMP354  Analysis of Algorithms

## Assignment 1

Consider Problem 1.9(c) :Implement Euclid’s Extended algorithm and run an experiment to verify this claim.

There is a typo: instead of  ```min{m,n}```, it should be ```min{(m)_b,(n)_b}```, that is, the running time ought to be bound in terms of the length of the binary encoding of the inputs, not their value.

The relationship between number of steps and binary lenght is shown by the graph below:

![alt text](https://github.com/DJones0101/COMP354/blob/master/a1/graph.png)



---

## Assignment 2

Please submit one assignment per group; form the groups at the beginning of the course, and
work together on all assignments (except the final exam which will be submitted individually).
Prim’s algorithm for MCSTs grows a tree in a natural way, starting from an arbitrary root;
at each stage it adds a new branch to the already constructed tree. The algorithm stops when
all nodes have been reached:

![alt text](https://github.com/DJones0101/COMP354/blob/master/a2/Prims.png)

Answer the following questions:
1. Compare what happens in Kruskal’s algorithm versus Prim’s algorithm if we run them
on a graph that is not connected.
2. Adapt Prim’s algorithm to graphs that may include edges of negative costs; give an
example of an application where negative costs may occur naturally.
3. A binary heap data structure is an array that we can view naturally as a nearly complete
binary tree. Each node of the tree corresponds to an element in the array, as shown
below:

![alt text](https://github.com/DJones0101/COMP354/blob/master/a2/heap.png)

note that the array has the following interesting structure: the parent of i is bi/2c and
the left child of i is 2i and the right child of i is (2i + 1).
With the binary heap data structure we can implement line 4. efficiently, that is, find
the cheapest e. To this end, implement a min-priority queue B, which, during the
execution of Prim’s algorithm, keeps track of all the vertices that are not in the tree
T. The min-priority queue B uses the following key attribute: minimum weight of any
edge connecting the vertex to T (and ∞ if no such edge exists).
Describe the details of the above scheme, and implement it in Python 3






---
## Assignment 3

