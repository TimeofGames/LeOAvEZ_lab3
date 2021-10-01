import Exceptions_Node


class Node():
    def __init__(self, name=None, data=None, index=None):
        self._name = name
        self._data = str(data)
        self._index = index
        self._flag = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def data(self):
        return str(self._data)

    @data.setter
    def data(self, new_data):
        self._data = str(new_data)

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, new_index):
        self._index = new_index

    @property
    def flag(self):
        return self._flag

    def node_name_update(self, node):
        self._name = self._name + node.name
        return self._index

    def node_data_update(self, node):
        self._data = self.data + node.data

    def __eq__(self, other):
        if isinstance(other, Node):
            return self._equal(other.data)
        else:
            return self._equal(other)

    def _equal(self, other):
        try:
            if self.data == other:
                return True
            else:
                return False
        except TypeError:
            return False

    def __hash__(self):
        return hash(self.data)

    def add_flag(self, flag):
        self._flag.append(flag)

    def remove_flag(self, flag):
        self._flag.remove(flag)
