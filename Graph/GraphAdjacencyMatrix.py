############################################
# Adjacency Matrix representation of Graph #
############################################

class Graph:
    # initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        self.size = size
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        
    # add edges
    def addEdge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    
    # remove edges
    def removeEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
    
    # print the matrix
    def printMatrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val), end=" ")
            print()

def main():
    g = Graph(5)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(1, 2)

    g.removeEdge(2, 1)

    g.printMatrix()

if __name__ == "__main__":
    main()