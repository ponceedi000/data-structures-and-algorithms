from code_challenges.graph.graph import Graph


def test_list_output():
    g = Graph()
    v1=g.add_node('a')
    v2=g.add_node('b')
    v3=g.add_node('c')
    v4=g.add_node('d')
    v5=g.add_node('e')

    g.add_edge(v1,v2)
    g.add_edge(v2,v4)
    g.add_edge(v4,v5)
    g.add_edge(v1,v5)
    g.add_edge(v1,v3)
    g.add_edge(v3,v5)

    expected = g.breadthfirst(v1)
    actual = ['a', 'b', 'd', 'e', 'c']
    assert actual == expected
