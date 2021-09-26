class GraphError(Exception):
    def __str__(self):
        return "Impossible action"


class RibNotIncludedError(GraphError):
    def __str__(self):
        return "No rib"


class NodeNotIncluded(GraphError):
    def __str__(self):
        return "Node not included"


class NodeAlreadyIncluded(GraphError):
    def __str__(self):
        return "Node already included"


class NodeNotIncludedError(GraphError):
    def __str__(self):
        return "Node not included"


class NodeError(GraphError):
    def __str__(self):
        return "This is not a node"
