from code_challenges.trees.queue import Queue

class Graph:

    def __init__(self):
        self.adjacency_list = {}
        # key will be the node, value adj node with a value of the edge

    def size(self):
        return len(self.adjacency_list)
            # Arguments: none
            # Returns the total number of nodes in the graph

    def get_node(self):
        return list(self.adjacency_list)
            # Arguments: none
            # Returns all nodes in graph as a collection (set, list, or similar)

    def add_node(self, value):
        v = Vertex(value)
        self.adjacency_list[v] = []
        return v
            # Arguments: value
            # Returns: The added node
            # Add a node to the graph or add to adj list

    def add_edge(self, start_vertex, end_vertex, weight=1):
        if end_vertex not in self.adjacency_list:
            raise KeyError
        self.adjacency_list[start_vertex].append(Edge(end_vertex, weight))


            # Arguments: 2 nodes to be connected by the edge, weight (optional)
            # Returns: nothing
            # Adds a new edge between two nodes in the graph
            # If specified, assign a weight to the edge
            # Both nodes should already be in the Graph


    def get_neighbor(self, vertex):
        return self.adjacency_list[vertex]
            # Arguments: node
            # Returns a collection of edges connected to the given node
                # Include the weight of connection in returned collection


    def breadthfirst(self, vertex):
        nodes = list()
        breadth = Queue()
        visited = set()
        breadth.enqueue(vertex)
        visited.add(vertex)

        while breadth:
            front = breadth.dequeue()
            nodes.append(front)

            for child in nodes:
                if child not in visited:
                    visited.add(child)
                    breadth.enqueue(child)
        return nodes



class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex,weight=1):
        self.vertex = vertex
        self.weight = weight
