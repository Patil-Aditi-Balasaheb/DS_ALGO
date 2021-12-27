############################################
# Adjacency List representation of Graph #
############################################

class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:
    def __init__(self, num):
        self.v = num
        self.graph = [None] * self.v
        
    # add edges
    def addEdge(self, v1, v2):
        node = AdjNode(v2)
        node.next = self.graph[v1]
        self.graph[v1] = node
        
        node = AdjNode(v1)
        node.next = self.graph[v2]
        self.graph[v2] = node
    
    # print the matrix
    def printMatrix(self):
        for i in range(self.v):
            print("Vertex", i,":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print()


def main():
    v = 5
    graph = Graph(v)
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(0, 3)
    graph.addEdge(1, 2)
    graph.printMatrix()


if __name__ == "__main__":
    main()