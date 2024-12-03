from typing import List
from heapq import heappop, heappush

class Edge:
    dest: int
    cost: int

    def __init__(self, dest: int, cost: int):
        self.dest = dest
        self.cost = cost

class Node:
    value: int
    edges: List[Edge]

    def __init__(self, value: int, edges: List[Edge]):
        self.value = value
        self.edges = edges

class Graph:
    values: List[List[int]]
    number_nodes: int
    adjacent_list: List[Node]

    def __init__(self, values: List[List[int]], number_nodes):
        self.values = values
        self.number_nodes = number_nodes
        self.adjacent_list = [None] * (number_nodes + 1)

    def build_graph(self):
        for i in range(1, self.number_nodes + 1):
            self.adjacent_list[i] = Node(i, [])

        for source, dest, cost in self.values:
            edge_source = Edge(dest, cost)
            self.adjacent_list[source].edges.append(edge_source)

class Dijkstra:
    graph: Graph
    heapq: List
    visiteds : dict

    def __init__(self, graph: Graph):
        self.graph = graph
        self.heapq = []
        self.visiteds = {}

    def find_min_val(self, start: int, end: int) -> int:
        heappush(self.heapq, (0, start))
        self.visiteds = {}

        while self.heapq:
            cost, node_value = heappop(self.heapq)

            if node_value in self.visiteds and self.visiteds[node_value] <= cost:
                continue

            self.visiteds[node_value] = cost

            if node_value == end:
                return cost

            for edge in self.graph.adjacent_list[node_value].edges:
                neighbor = edge.dest
                cost_to_dest = edge.cost
                new_cost = cost + cost_to_dest

                if neighbor not in self.visiteds or self.visiteds[neighbor] > new_cost:
                    heappush(self.heapq, (new_cost, neighbor))

        return -1

def queries_result(edges, n, start) -> int:
    graph = Graph(edges, n)
    graph.build_graph()

    dijkstra = Dijkstra(graph)

    max_cost = -1

    for end in range(1, n + 1):
        if start != end:
            min_val = dijkstra.find_min_val(start, end)
            if min_val == -1:
                return -1
            max_cost = max(max_cost, min_val)

    return max_cost


#Adicione a linha abaixo em networkDelayTime na classe Solution o leetcode para testar
#return queries_result(times, n, k)

""" Descomente para testar no leetcode
edges = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(queries_result(edges,n, k))

edges = [[1,2,1]]
n = 2
k = 1
print(queries_result(edges,n, k))

edges = [[1,2,1]]
n = 2
k = 2
print(queries_result(edges,n, k))
"""
