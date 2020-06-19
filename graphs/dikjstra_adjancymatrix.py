# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

# Library for INT_MAX
import sys


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.parent = {}
        self.short_dist = {}
        self.curr_dist = {}

    def printSolution(self, dist):
        print
        "Vertex \tDistance from Source"
        for node in range(self.V):
            print
            node, "\t", dist[node]

        # A utility function to find the vertex with

    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistanceKey(self):
        m = float('inf')
        to_r = -1
        for i in list(self.curr_dist.keys()):
            if self.curr_dist[i] < m:
                print(self.curr_dist)
                m = self.curr_dist[i]
                to_r = i
        return to_r

    # Funtion that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):
        for i in range(self.V):
            self.curr_dist[i] = float('inf')
        self.curr_dist[src] = 0
        while len(self.curr_dist.keys()):
            min_idx = self.minDistanceKey()
            self.short_dist[min_idx] = self.curr_dist[min_idx]
            del self.curr_dist[min_idx]
            for i in range(self.V):
                if self.short_dist.get(i) is not None:
                    continue
                if self.graph[min_idx][i] == 0:
                    continue
                if (self.graph[min_idx][i] + self.short_dist[min_idx]) < (self.curr_dist[i]):
                    self.curr_dist[i] = self.graph[min_idx][i] + self.short_dist[min_idx]
                    self.parent[i] = min_idx
        print(self.short_dist)
        self.printSolution(self.short_dist)


# Driver program
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ];

g.dijkstra(0);
