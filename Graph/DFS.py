###########################################
# Depth First Search or BFS for a Graph #
###########################################

# Time complexity: O(V+E), where V is no. of vertices and E is no. of edges in graph
# Space complexity: O(V), since an extra visited array of size V is required

'''
Depth First Traversal (or Search) for a graph is similar to Depth First Traversal of a tree. The only catch here is, unlike trees, graphs may contain cycles (a node may be visited twice). To avoid processing a node more than once, use a boolean visited array.
eg.
Input: n = 4, e = 6 
0 -> 1, 0 -> 2, 1 -> 2, 2 -> 0, 2 -> 3, 3 -> 3 
Output: DFS from vertex 1 : 1 2 0 3 

eg.
Input: n = 4, e = 6 
2 -> 0, 0 -> 2, 1 -> 2, 0 -> 1, 3 -> 3, 1 -> 3 
Output: DFS from vertex 2 : 2 0 1 3 
'''

# DFS traversal for complete graph

from collections import defaultdict

# class that represents a directed graph using adjacency list representation
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # default dictionary to store graph
    
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    # function used by DFS
    def DFSUtil(self, v, visited):
        # mark the current node as visited and print it
        visited.add(v)
        print(v, end=" ")

        # recur for all the vertices adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    # function to do DFS traversal
    # it uses recursive DFSUtil()
    def DFS(self):
        # set to store visited vertices
        visited = set()

        # call the recursive helper function to print 
        # DFS traversal starting from all vertices one by one
        for vertex in self.graph:
            if vertex not in visited:
                self.DFSUtil(vertex, visited)


g = Graph()
'''
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
'''

g.addEdge(2, 0)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(0, 1)
g.addEdge(3, 3)
g.addEdge(1, 3)
g.DFS()