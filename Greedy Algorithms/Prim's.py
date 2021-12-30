################################################################
# Prim's Minimum Spanning Tree Algorithm (Greedy Algorithm) #
################################################################

# The time complexity of Prim's algorithm is O(ElogV)
# But the code implemented here has O(V^2) time complexity

'''
Prim's algorithm is a minimum spanning tree algorithm that takes a graph as input and finds the subset of the edges of that graph which
- form a tree that includes every vertex
- has the minimum sum of weights among all the trees that can be formed from the graph

It falls under a class of algorithms called greedy algorithms that find the local optimum in the hopes of finding a global optimum.

The steps for implementing Prim's algorithm are as follows:
1. Initialize the minimum spanning tree with a vertex chosen at random.
2. Find all the edges that connect the tree to new vertices, find the minimum and add it to the tree
3. Keep repeating step 2 until we get a minimum spanning tree

		A		D
		|\4    / \3
		| \  3/	  \
		|  \ /	4  \
	   4|   C ----- F	Step 1 : Start with a weighted graph
		|  / \	   /
		| /2  \	  /3
		|/	  2\ /
		B 		E

	        C       	Step 2 : Choose a vertex

	        C  	
		   /  
		  /2            Step 3 : Choose the shortest edge from this vertex and add it
		 /	  
		B

	        C  	
		   / \ 
		  /2  \2        Step 4 : Choose the nearest vertex not yet in the solution
		 /	   \
		B       E

	        C  	    F
		   / \     /
		  /2  \2  /3    Step 5 : Choose the nearest edge not yet in the solution, if there are multiple choices, choose one at random
		 /	   \ /
		B       E        

		A		D
		 \4    / 
		  \  3/	  
		   \ /	
	        C       F	Step 6 : Repeat until you have a spanning tree
		   / \	   /
		  /2  \	  /3
		 /	  2\ /
		B 		E

'''

# Python program for Prim's algorithm 
# the program is for adjacnecy matrix representation of the graph

import sys  # library for using INT_MAX

# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    # function to print the constructed MST stored in parent[]
    def printMST(self, parent):
        minCost = 0
        print("Edge\t Weight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
            minCost += self.graph[i][parent[i]]
        
        print("Minimum cost is", minCost)
        
    # function to find the vertex with minimum distance value,
    # from the set of vertices not yet included in shortest path tree
    def minKey(self, key, mstSet):
        # initialize min value
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        
        return min_index
    
    # function to construct and print MST for a graph
    # represented using adjacency matrix representation
    def primMST(self):
        # key values used to pick minimum weight edge
        key = [sys.maxsize] * self.V
        
        # array to store constructed MST
        parent = [None] * self.V

        # make key 0 so that this vertex is picked as first vertex
        key[0] = 0

        mstSet = [False] * self.V

        # first node is always the root so it has not parent
        parent[0] = -1

        for cout in range(self.V):
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)

            # Put the minimum distance vertex in the shortest path tree
            mstSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):

                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
            
        self.printMST(parent)


g = Graph(5)
'''
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]
'''
g.graph = [[0, 9, 75, 0, 0],
           [9, 0, 95, 19, 42],
           [75, 95, 0, 51, 66],
           [0, 19, 51, 0, 31],
           [0, 42, 66, 31, 0]]
           
g.primMST()