from code_challenges.graph.graph import Graph, Vertex
import pytest

def test_add_node():
    g = Graph()
    added_vertex = g.add_node("test")
    expected = "test"
    actual = added_vertex.value
    assert actual == expected

def test_size_empty():
    g = Graph()
    expected = 0
    actual = g.size()
    assert actual == expected

def test_get_nodes_empty():
    g = Graph()
    expected = []
    actual = g.get_node()
    assert actual == expected

def test_size():
    g = Graph()
    g.add_node("test")
    expected = 1
    actual = g.size()
    assert actual == expected

def test_get_nodes():
    g = Graph()
    apple = g.add_node("apple")
    banana = g.add_node("banana")
    mango = Vertex("mango")
    expected = 2
    actual = len(g.get_node())
    assert actual == expected

def test_add_edge_simple():
    g = Graph()
    apple = g.add_node("apple")
    banana = g.add_node("banana")
    g.add_edge(apple, banana, 5)
    assert True

def test_add_edge_with_neighbors():
    g = Graph()
    apple = g.add_node("apple")
    banana = g.add_node("banana")
    g.add_edge(apple, banana, 5)

    neighbors = g.get_neighbor(apple)
    assert len(neighbors) == 1
    edge = neighbors[0]
    assert edge.vertex == banana
    assert edge.weight == 5

def test_bouquet():
    g = Graph()
    apple = g.add_node("apple")
    g.add_edge(apple, apple, 10)
    neighbors = g.get_neighbor(apple)
    assert len(neighbors) == 1
    edge = neighbors[0]
    assert edge.vertex == apple
    assert edge.weight == 10

def test_add_edge_interloper_start():
    g = Graph()
    start = Vertex("start")
    end = g.add_node("end")
    with pytest.raises(KeyError):
        g.add_edge(start, end)

def test_add_edge_interloper_end():
    g = Graph()
    end = Vertex("end")
    start = g.add_node("start")
    with pytest.raises(KeyError):
        g.add_edge(start, end)

def test_get_neighbors_weight():
    g = Graph()
    banana = g.add_node("banana")
    apple = g.add_node("apple")
    g.add_edge(apple, banana, 44)
    neighbors = g.get_neighbor(apple)
    assert len(neighbors) == 1
    neighbor_edge = neighbors[0]
    assert neighbor_edge.vertex.value == "banana"
    assert neighbor_edge.weight == 44
