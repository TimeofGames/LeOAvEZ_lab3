import Exceptions_Graph
import Node
import Matrix
import AdjacencyList


class Graph():
    def __init__(self, name, nodes=None):
        self.name = str(name)
        self._last_element = 0
        self._nodes = list()
        self._matrix = Matrix.Matrix()
        self._adjacency_list = AdjacencyList.AdjacencyList()
        if nodes is not None:
            if isinstance(nodes, list):
                for i in nodes:
                    self.add_node(i)
            else:
                raise Exceptions_Graph.GraphError

    def get_index_on_data(self, data, default=None):
        for i in self._nodes:
            if i == data:
                return i.index
        return default

    def add_node(self, data, name=None):
        if not (self._check_node_in_graph(data)):
            if name is None:
                name = self.name + str(self._last_element)
            node = Node.Node(data=data, name=name, index=self._last_element)
            self._nodes.append(node)
            self._last_element += 1
            self._matrix.add_node(self._nodes[-1])
            self._adjacency_list.add_node(self._nodes[-1])
            return node.index
        else:
            raise Exceptions_Graph.NodeAlreadyIncluded

    def _check_node_in_graph(self, data):
        for i in [i.data for i in self._nodes]:
            try:
                if data == i:
                    return True
            except TypeError:
                return False
        return False

    def del_node(self, index):
        if [i.data for i in self._nodes]:
            self._matrix.del_node(self._nodes[index])
            self._adjacency_list.del_node(self._nodes[index])
            self._nodes.pop(index)
            self._index_update()
        else:
            raise Exceptions_Graph.NodeNotIncludedError

    def _index_update(self):
        for i in range(len(self._nodes)):
            self._nodes[i].index = i

    def print(self):
        print("Матрица смежности")
        self._matrix.print()
        print("Список смежности")
        self._adjacency_list.print()
        print([i.name for i in self._nodes])

    def connect(self, from_node, to_node, weight=1):
        self.connect_dir(from_node, to_node, weight)
        self.connect_dir(from_node, to_node, weight)

    def connect_dir(self, from_node, to_node, weight=1):
        from_node, to_node = self._node_review(from_node, to_node)
        self._matrix.connect_dir(from_node, to_node, weight)
        self._adjacency_list.connect_dir(from_node, to_node, weight)

    def disconnect(self, from_node, to_node, weight=1):
        self.disconnect_dir(from_node, to_node, weight)
        self.disconnect_dir(to_node, from_node, weight)

    def disconnect_dir(self, from_node, to_node, weight_input=1):
        from_node, to_node = self._node_review(from_node, to_node)
        try:
            self._matrix.disconnect_dir(from_node, to_node, weight_input)
            self._adjacency_list.disconnect_dir(from_node, to_node, weight_input)
        except ValueError:
            raise Exceptions_Graph.RibNotIncludedError

    def convert_matrix_to_adj_list(self):
        return self._matrix.convert_to_adj_list()

    def convert_adj_list_to_matrix(self):
        return self._adjacency_list.convert_to_matrix()

    def node_association(self, from_node, to_node):
        from_node, to_node = self._node_review(from_node, to_node)
        self._matrix.node_association(from_node, to_node)
        self._adjacency_list.node_association(from_node, to_node)
        self.del_node(from_node.index)

    def rib_retraction(self, from_node, to_node, weight=1):
        from_node, to_node = self._node_review(from_node, to_node)
        try:
            self._matrix.rib_retraction(from_node, to_node, weight)
            self._adjacency_list.rib_retraction(from_node, to_node, weight)
        except Exceptions_Graph.RibNotIncludedError:
            raise Exceptions_Graph.RibNotIncludedError
        self.del_node(from_node.index)

    def _node_review(self,*nodes):
        array = []
        for node in nodes:
            if node is None:
                raise Exceptions_Graph.NodeNotIncludedError
            else:
                array.append(self._nodes[node])
        return array

    def node_duplication(self, from_node):
        from_node = self._node_review(from_node)
        self.add_node(str(from_node[0].data)+'d', name=from_node[0].name + 'd')
        self._matrix.node_duplication(from_node[0], self._nodes[-1])
        self._adjacency_list.node_duplication(from_node[0], self._nodes[-1])
