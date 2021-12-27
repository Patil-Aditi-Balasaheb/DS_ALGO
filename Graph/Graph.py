#########
# Graph #
#########

'''
A graph data structure is a collection of nodes that have data and are connected to other nodes.
More precisely, a graph is a data structure (V, E) that consists of
- A collection of vertices V
- A collection of edges E, represented as ordered pairs of vertices (u,v)

    0 ------ 3
    |\                  In the graph, 
    | \                 V = {0, 1, 2, 3}
    |  2                E = {(0,1), (0,2), (0,3), (1,2)}
    | /                 G = {V, E}
    |/
    1

Graph Terminology
- Adjacency: A vertex is said to be adjacent to another vertex if there is an edge connecting them. Vertices 2 and 3 are not adjacent because there is no edge between them.
- Path: A sequence of edges that allows you to go from vertex A to vertex B is called a path. 0-1, 1-2 and 0-2 are paths from vertex 0 to vertex 2.
- Directed Graph: A graph in which an edge (u,v) doesn't necessarily mean that there is an edge (v, u) as well. The edges in such a graph are represented by arrows to show the direction of the edge.

Graph Representation
Graphs are commonly represented in two ways:
1. Adjacency Matrix
   An adjacency matrix is a 2D array of V x V vertices. Each row and column represent a vertex.
   If the value of any element a[i][j] is 1, it represents that there is an edge connecting vertex i and vertex j.

   The adjacency matrix for the above graph is
        __|_0_|_1_|_2_|_3_|
        0 | 0 | 1 | 1 | 1 |
        1 | 1 | 0 | 1 | 0 |        Graph adjacency matrix
        2 | 1 | 1 | 0 | 0 | 
        3 | 1 | 0 | 0 | 0 |

2. Adjacency List
   An adjacency list represents a graph as an array of linked lists.
   The index of the array represents a vertex and each element in its linked list represents the other vertices that form an edge with the vertex.
   The adjacency list for the graph is as follows:
   
        | 0 | ----> | 1 |   | ----> | 2 |   | ----> | 3 |   |
        | 1 | ----> | 0 |   | ----> | 2 |   |
        | 2 | ----> | 0 |   | ----> | 1 |   |
        | 3 | ----> | 0 |   |
        
        Adjacency list representation

Graph Operations
The most common graph operations are:
- Check if the element is present in the graph
- Graph Traversal
- Add elements(vertex, edges) to graph
- Finding the path from one vertex to another
'''

# Graph implementation using dictionary in python

# class for graph
class Graph:
    
    # constructor for initializing
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    # get the keys of the dictionary i.e, vertices of graph
    def getVertices(self):
        return list(self.gdict.keys())
    
    # get the edges of graph
    def edges(self):
        edgename = []
        
        # iterate through the vertices(keys)
        for v in self.gdict:
            # iterate through the values for each key
            for nv in self.gdict[v]:
                if {nv,v} not in edgename:
                    edgename.append({v,nv})
        return edgename
    
    # add a new vertex to the graph
    def addVertex(self,v):
        if v not in self.gdict:
            self.gdict[v] = []
    
    # add the new edge
    def AddEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]


# create the dictionary with graph elements
graph_elements = {
    "a":["b","c"],
    "b":["a","d"],
    "c":["a","d"],
    "d":["e"],
    "e":["d"]
}  

g = Graph(graph_elements)
print("Graph Vertices:", g.getVertices())
print("Edges:", *g.edges())

g.addVertex("f")
print("\nGraph Vertices:", g.getVertices())

g.AddEdge({'a','e'})
g.AddEdge({'a','c'})
print("Edges:", *g.edges())