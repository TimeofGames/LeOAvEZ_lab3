class NodeError(Exception):
    def __str__(self):
        return "This isn't node"


class NodeAlreadyIncluded(NodeError):
    def __str__(self):
        return "Node already included"


class GraphError(Exception):
    def __str__(self):
        return "Impossible action"


class RibRetractionError(GraphError):
    def __str__(self):
        return "No rib"


class NodeNotIncluded(GraphError):
    def __str__(self):
        return "Node not included"


class Node():
    def __init__(self, data=None, index=None):
        self._data = data
        self._index = index

    @property
    def data(self):
        return self._data

    @property
    def index(self):
        return self._index

    @data.setter
    def data(self, data):
        self._data = data

    @index.setter
    def index(self, index):
        self._index = index


class Graph():
    def __init__(self):
        self._row = 0
        self._col = 0
        self._nodes = []
        self._matrix = []
        self._adjacency_list = dict()

    @property
    def row(self):
        return self._row

    @property
    def col(self):
        return self._col

    @property
    def nodes(self):
        return self._nodes

    @row.setter
    def row(self, row):
        self._row = row

    @col.setter
    def col(self, col):
        self._col = col

    @nodes.setter
    def nodes(self, nodes):
        self._nodes = nodes

    def check_node(self, node):
        for i in self._nodes:
            if id(i) == id(node):
                return True
        return False

    def add_node(self, node):
        if not (self.check_node(node)):
            if isinstance(node, Node):
                self._nodes.append(node)
                node.index = len(self._nodes) - 1
                self._matrix_update(1)
                self._adjacency_list[node] = list()
            else:
                raise NodeError
        else:
            raise NodeAlreadyIncluded

    def _matrix_update(self, add_nodes):
        for i in self._matrix:
            for _ in range(add_nodes):
                i.append([])
        for i in range(add_nodes):
            self._matrix.append([[] for _ in range(len(self._nodes))])

    def connect(self, node1, node2, weight=1):
        self.connect_dir(node1, node2, weight)
        self.connect_dir(node2, node1, weight)

    def connect_dir(self, node1, node2, weight=1):
        self._adjacency_list[node1].append(node2)
        node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
        self._matrix[node1][node2].append(weight)

    def disconnect(self, node1, node2):
        self.disconnect_dir(node1, node2)
        self.disconnect_dir(node2, node1)

    def disconnect_dir(self, node1, node2):
        weight = self._matrix[node1.index][node2.index].pop()
        self._adjacency_list[node1].remove(node2)
        return weight

    def get_index_from_node(self, node):
        if not isinstance(node, Node) and not isinstance(node, int):
            raise ValueError("node must be an integer or a Node object")
        if isinstance(node, int):
            return node
        else:
            return node.index

    def print_matrix(self):
        for node in self._nodes:
            print("   " + node.data, end="")
        print()
        for i in range(len(self._matrix)):
            print(str(self.nodes[i].data) + " " + str(self._matrix[i])[1:-1])

    def print_list(self):
        for i in self.nodes:
            print(str(i.data) + ":", end="")
            for j in self._adjacency_list[i]:
                print(str(j.data) + ", ", end="")
            print()

    def _index_update(self):
        for i in range(len(self.nodes)):
            self._nodes[i].index = i

    def vertex_identification(self, node1, node2):
        node2_str = self._matrix[node2.index]
        node2_row = []
        for i in self._matrix:
            node2_row.append(i[node2.index])
        for i in range(len(node2_str)):
            if len(node2_str[i]) != 0 and self._nodes[i] is not node1:
                for _ in range(len(node2_str[i])):
                    weight = self.disconnect_dir(node2, self._nodes[i])
                    self.connect_dir(node1, self._nodes[i], weight=weight)
        for i in range(len(node2_row)):
            if len(node2_row[i]) != 0 and self._nodes[i] is not node1:
                for _ in range(len(node2_row[i])):
                    weight = self.disconnect_dir(self._nodes[i], node2)
                    self.connect_dir(self._nodes[i], node1, weight=weight)
        while node2 in self._adjacency_list[node1]:
            self._adjacency_list[node1].remove(node2)
        self._matrix.pop(node2.index)
        for i in self._matrix:
            i.pop(node2.index)
        self._nodes.pop(node2.index)
        self._adjacency_list.pop(node2)
        self._index_update()

    def rib_retraction(self, node1, node2):
        if 1 in self._matrix[node1.index][node2.index]:
            self.vertex_identification(node1, node2)
        else:
            raise RibRetractionError

    def split_vertices(self, node):
        if node in self._nodes:
            self._nodes.append(Node(data=node.data + "d"))
            self._index_update()
            self._matrix_update(1)
        else:
            raise NodeNotIncluded
        self._adjacency_list[self._nodes[-1]] = list()
        for i in range(len(self._matrix)):
            if len(self._matrix[i][node.index]) != 0:
                for _ in range(len(self._matrix[i][node.index])):
                    self.connect_dir(self._nodes[-1], self._nodes[i])
            if len(self._matrix[node.index][i]) != 0:
                for _ in range(len(self._matrix[node.index][i])):
                    self.connect_dir(self._nodes[i], self._nodes[-1])
        return self._nodes[-1]


matrix = Graph()
nodes = []
for i in range(10):
    nodes.append(Node(data="V" + str(i)))
    matrix.add_node(nodes[i])

matrix.connect(nodes[1], nodes[2])
matrix.connect(nodes[3], nodes[2])
matrix.connect(nodes[3], nodes[9])
matrix.print_matrix()
matrix.print_list()
nodes.append(matrix.split_vertices(nodes[1]))
matrix.print_matrix()
matrix.print_list()
