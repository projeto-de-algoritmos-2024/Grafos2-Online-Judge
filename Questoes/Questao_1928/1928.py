from typing import List
from heapq import heappop, heappush
from collections import defaultdict

class Edge:
    dest: int
    time_travel: int

    def __init__(self, dest: int, time_travel: int):
        self.dest = dest
        self.time_travel = time_travel

class Node:
    value: int
    pass_fee: int
    edges: List[Edge]

    def __init__(self, value: int, pass_fee: int, edges: List[Edge]):
        self.value = value
        self.pass_fee = pass_fee
        self.edges = edges

class Graph:
    values: List[List[int]]
    pass_fees: List[int]
    adjacent_list: List[Node]

    def __init__(self, values: List[List[int]], pass_fees: List[int]):
        self.values = values
        self.pass_fees = pass_fees
        self.adjacent_list = []

    def build_graph(self):
        for i in range(len(self.pass_fees)):
            self.adjacent_list.append(Node(i, self.pass_fees[i], []))

        for source, dest, time_travel in self.values:
            edge_source = Edge(dest, time_travel)
            edge_dest = Edge(source, time_travel)
            self.adjacent_list[source].edges.append(edge_source)
            self.adjacent_list[dest].edges.append(edge_dest)

class Dijkstra:
    graph: Graph
    heapq: List
    visiteds: dict

    def __init__(self, graph: Graph):
        self.graph = graph
        self.heapq = [(graph.adjacent_list[0].pass_fee, 0, 0)]
        self.visiteds = {}

    def find_min_val(self, maxTime: int) -> int:
        
        while self.heapq:
            total_cost, time_taken, node_value = heappop(self.heapq)

            if node_value == len(self.graph.pass_fees) - 1:
                return total_cost

            if node_value in self.visiteds and self.visiteds[node_value] <= time_taken:
                continue

            self.visiteds[node_value] = time_taken

            for edge in self.graph.adjacent_list[node_value].edges:
                neighbor = edge.dest
                travel_time = edge.time_travel
                new_time = time_taken + travel_time
                if new_time <= maxTime:
                    new_cost = total_cost + self.graph.adjacent_list[neighbor].pass_fee
                    heappush(self.heapq, (new_cost, new_time, neighbor))

        return -1
