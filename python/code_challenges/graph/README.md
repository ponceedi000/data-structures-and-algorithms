# Graphs
- > In computer science, a graph is an abstract data type that is meant to implement the undirected graph and directed graph concepts from the field of graph theory within mathematics. A graph data structure consists of a finite (and possibly mutable) set of vertices (also called nodes or points), together with a set of unordered pairs of these vertices for an undirected graph or a set of ordered pairs for a directed graph. These pairs are known as edges (also called links or lines), and for a directed graph are also known as edges but also sometimes arrows or arcs. The vertices may be part of the graph structure, or may be external entities represented by integer indices or references. A graph data structure may also associate to each edge some edge value, such as a symbolic label or a numeric attribute (cost, capacity, length, etc.). [Wikipedia](https://en.wikipedia.org/wiki/Graph_(abstract_data_type))

## Links
- [Graph Implementation](graph.py)
- [Graph Tests](tests/../../../tests/test_graph.py)
- [Pull Request](https://github.com/ponceedi000/data-structures-and-algorithms/pull/39)

## Challenge
### Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

- add node
  * Arguments: value
  * Returns: The added node
  * Add a node to the graph
- add edge
  * Arguments: 2 nodes to be connected by the edge, weight (optional)
  * Returns: nothing
  * Adds a new edge between two nodes in the graph
  * If specified, assign a weight to the edge
  * Both nodes should already be in the Graph
- get nodes
  * Arguments: none
  * Returns all of the nodes in the graph as a collection (set, list, or similar)
- get neighbors
  * Arguments: node
  * Returns a collection of edges connected to the given node
    * Include the weight of the connection in the returned collection
- size
  * Arguments: none
  * Returns the total number of nodes in the graph

## Approach & Efficiency
- Instead of writing all of my code first followed by testing, I decided write tests per new class method. This broke everything down into smaller steps which helped a lot.

## API
- add node
  - Time: O(1)
- add edge
  - Time O(1)
- get nodes
- get neighbors
- size
