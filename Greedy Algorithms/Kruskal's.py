################################################################
# Kruskal's Minimum Spanning Tree Algorithm (Greedy Algorithm) #
################################################################

# The time complexity Of Kruskal's Algorithm is: O(E log E)
# Time Complexity: O(ElogE) or O(ElogV). Sorting of edges takes O(ELogE) time. After sorting, we iterate through all edges and apply the find-union algorithm. The find and union operations can take at most O(LogV) time. So overall complexity is O(ELogE + ELogV) time. The value of E can be at most O(V2), so O(LogV) is O(LogE) the same. Therefore, the overall time complexity is O(ElogE) or O(ElogV)

'''
A minimum spanning tree (MST) or minimum weight spanning tree for a weighted, connected, undirected graph is a spanning tree with a weight less than or equal to the weight of every other spanning tree. The weight of a spanning tree is the sum of weights given to each edge of the spanning tree.

How many edges does a minimum spanning tree has? 
A minimum spanning tree has (V - 1) edges where V is the number of vertices in the given graph. 

Kruskal's algorithm is a minimum spanning tree algorithm that takes a graph as input and finds the subset of the edges of that graph which
- form a tree that includes every vertex
- has the minimum sum of weights among all the trees that can be formed from the graph

The steps for implementing Kruskal's algorithm are as follows:
1. Sort all the edges from low weight to high
2. Take the edge with the lowest weight and add it to the spanning tree. If adding the edge created a cycle, then reject this edge.
3. Keep adding edges until we reach all vertices.

		O		O
		|\4    / \3
		| \  3/	  \
		|  \ /	4  \
	   4|   O ----- O	Step 1 : Start with a weighted graph
		|  / \	   /
		| /2  \	  /3
		|/	  2\ /
		O 		O

   	        O 
		   /
		  /2  			Step 2 : Choose the edge with the least weight, if there are more than 1, choose anyone
		 /	  
		O 		

   	      	O 
		   / \	  
		  /2  \	  		Step 3 : Choose the next shortest edge and add it
		 /	  2\ 
		O 		O
	
				O
		       / 
		     3/	 
		     /
	        O 			Step 4 : Choose the next shortest edge that doesn't create a cycle and add it
		   / \	   
		  /2  \	 
		 /	  2\ 
		O 		O

				O
		       / 
		     3/	 
		     /
	        O 		O	Step 5 : Choose the next shortest edge that doesn't create a cycle and add it
		   / \	   /
		  /2  \	  /3
		 /	  2\ / 
		O 		O

		O		O
		 \     / 
		 4\  3/	 
		   \ /
	        O 		O	Step 6 : Repeat until you have a spanning tree
		   / \	   /
		  /2  \	  /3
		 /	  2\ / 
		O 		O

'''

# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given connected,
# undirected and weighted graph

# Class to represent a graph
class Graph:

	def __init__(self, vertices):
		self.V = vertices   # No. of vertices
		self.graph = []     # default dictionary to store graph

	# function to add an edge to graph
	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])

	# A utility function to find set of an element i
	# (uses path compression technique)
	def find(self, parent, i):
		if parent[i] == i:
			return i
		return self.find(parent, parent[i])

	# A function that does union of two sets of x and y
	# (uses union by rank)
	def union(self, parent, rank, x, y):
		xroot = self.find(parent, x)
		yroot = self.find(parent, y)

		# Attach smaller rank tree under root of
		# high rank tree (Union by Rank)
		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot

		# If ranks are same, then make one as root
		# and increment its rank by one
		else:
			parent[yroot] = xroot
			rank[xroot] += 1

	# The main function to construct MST using Kruskal's algorithm
	def KruskalMST(self):

		result = []     # This will store the resultant MST
		
		# An index variable, used for sorted edges
		i = 0
		
		# An index variable, used for result[]
		e = 0

		# Step 1: Sort all the edges in
		# non-decreasing order of their
		# weight. If we are not allowed to change the
		# given graph, we can create a copy of graph
		self.graph = sorted(self.graph, key=lambda item: item[2])

		parent = []
		rank = []

		# Create V subsets with single elements
		for node in range(self.V):
			parent.append(node)
			rank.append(0)

		# Number of edges to be taken is equal to V-1
		while e < self.V - 1:

			# Step 2: Pick the smallest edge and increment
			# the index for next iteration
			u, v, w = self.graph[i]
			i = i + 1
			x = self.find(parent, u)
			y = self.find(parent, v)

			# If including this edge does't
			# cause cycle, include it in result
			# and increment the indexof result
			# for next edge
			if x != y:
				e = e + 1
				result.append([u, v, w])
				self.union(parent, rank, x, y)
			# Else discard the edge

		minimumCost = 0
		print ("Edges in the constructed MST")
		for u, v, weight in result:
			minimumCost += weight
			print("%d -- %d == %d" % (u, v, weight))
		print("Minimum Spanning Tree" , minimumCost)


'''
g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
'''

g = Graph(6)
g.addEdge(0, 1, 4)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 2)
g.addEdge(1, 0, 4)
g.addEdge(2, 0, 4)
g.addEdge(2, 1, 2)
g.addEdge(2, 3, 3)
g.addEdge(2, 5, 2)
g.addEdge(2, 4, 4)
g.addEdge(3, 2, 3)
g.addEdge(3, 4, 3)
g.addEdge(4, 2, 4)
g.addEdge(4, 3, 3)
g.addEdge(5, 2, 2)
g.addEdge(5, 4, 3)

# Function call
g.KruskalMST()