class NodeError(Exception):
    def __str__(self):
        return "This isn't node"


class NodeErrorAlreadyIncluded(NodeError):
    def __str__(self):
        return "Node already included"


class Node():
    def __init__(self, data, index=None):
        self._data = data
        self._index = index
        self._connects = dict()

    @property
    def data(self):
        return self._data

    @property
    def index(self):
        return self._index

    @property
    def connects(self):
        return self._connects

    @data.setter
    def data(self, data):
        self.data = data

    @index.setter
    def index(self, index):
        self._index = index

    def add_connect(self,connect):
        self._connects.update([(len(self.connects),connect.index)])

    def del_connect(self,index):
        self._connects.pop(index)

class Graph():
    def __init__(self, nodes=None):
        if nodes is None:
            self._row = 0
            self._col = 0
            self._nodes = []
            self._matrix = []
        else:
            self._row = len(nodes)
            self._col = len(nodes)
            self._nodes = nodes
            for i in range(len(self._nodes)):
                self._nodes[i].index = i - 1
            self._matrix = []

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
                self.matrix_update(1)
            else:
                raise NodeError
        else:
            raise NodeErrorAlreadyIncluded

    def matrix_update(self, add_nodes):
        for i in self._matrix:
            for _ in range(add_nodes):
                i.append([])
        for i in range(add_nodes):
            self._matrix.append([[] for _ in range(len(self._matrix) + add_nodes)])

    def connect(self, node1, node2, weight=1):
        self.connect_dir(node1, node2, weight)
        self.connect_dir(node2, node1, weight)

    def connect_dir(self, node1, node2, weight=1):
        node1.add_connect(node2)
        node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
        self._matrix[node1][node2].append(weight)

    def get_index_from_node(self, node):
        if not isinstance(node, Node) and not isinstance(node, int):
            raise ValueError("node must be an integer or a Node object")
        if isinstance(node, int):
            return node
        else:
            return node.index

    def print_matrix(self):
        for row in self._matrix:
            print(row)

    def convert_to_list(self):
        dictionary = dict()
        for node in self._nodes:
            connects = ()
            for i in range(len(node.connects)):
                connects = (node.connects.get(i)) + connects
            dictionary.update([node.index,connects])
        return dictionary


matrix = Graph()
nodes = []
for i in range(10):
    nodes.append(Node(i))
    matrix.add_node(nodes[i])

matrix.print_matrix()
print()
matrix.connect(nodes[2], nodes[0])

matrix.print_matrix()
print(matrix.convert_to_list())
