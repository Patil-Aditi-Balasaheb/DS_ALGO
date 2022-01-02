###############################################
# Dijkstra's Shortest Path Algorithm (Greedy) #
###############################################

# Time complexity: O(E log V) where, E is no. of edges and V is no. of vertices
# Space complexity: O(V)

'''
Given a graph and a source vertex in the graph, find the shortest paths from the source to all vertices in the given graph.
We maintain two sets, one set contains vertices included in the shortest-path tree, other set includes vertices not yet included in the shortest-path tree. At every step of the algorithm, we find a vertex that is in the other set (set of not yet included) and has a minimum distance from the source.

Time Complexity of the implementation is O(V^2). If the input graph is represented using adjacency list, it can be reduced to O(E log V) with the help of a binary heap.

Dijkstra's algorithm doesn't work for graphs with negative weight cycles. It may give correct results for a graph with negative edges but you must allow a vertex can be visited multiple times and that version will lose its fast time complexity. For graphs with negative weight edges and cycles, Bellman-Ford algorithm can be used

Dijkstra's Algorithm Applications
- To find the shortest path
- In social networking applications
- In a telephone network
- To find the locations in the map
'''

# library for inf
import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for col in range(vertices)] for row in range(vertices)]
    
    # function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):

        # initialize minimum distance for next node
        min = sys.maxsize

        # search nearest vertex not in the shortest path tree
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
        
        return min_index
    
    def printSolution(self, dist):
        print("Vertex\tDistance from source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0

        sptSet = [False] * self.V
        
        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to src in first iteration
            x = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[x] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
            
        self.printSolution(dist)


'''
g = Graph(9)
g.graph = [ [0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0] ]
'''

g = Graph(7)
g.graph = [ [0, 0, 1, 2, 0, 0, 0],
            [0, 0, 2, 0, 0, 3, 0],
            [1, 2, 0, 1, 3, 0, 0],
            [2, 0, 1, 0, 0, 0, 1],
            [0, 0, 3, 0, 0, 2, 0],
            [0, 3, 0, 0, 2, 0, 1],
            [0, 0, 0, 1, 0, 1, 0] ]

g.dijkstra(0)