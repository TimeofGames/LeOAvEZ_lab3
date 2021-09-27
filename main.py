from Graph import Graph

graph = Graph(name='V')
graph2 = Graph(name='X')

for i in range(5):
    graph.add_node(i)
    graph2.add_node(i)

graph.connect_dir(1, 2)
graph.connect_dir(2, 1)

graph3 = graph.annular_sum(graph2)
graph3.print()
