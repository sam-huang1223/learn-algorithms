class UF:
    def __init__(self, n):
        """ Initialize union-find data structure with N objects (0 to N-1) """
        self.data = [i for i in range(n)]
        self.tree_size = [1 for i in range(n)]

    def _get_root(self, value):
        """ Finds the root of any given object """
        initial_node = value
        while self.data[value] != value:
            value = self.data[value]
        self.compress_path(initial_node, value)
        return value

    def compress_path(self, node, root):
        """ attempts to minimize height of the tree by setting the parent of a node equal to the root of the node """
        while self.data[node] != node:
            node = self.data[node]
            self.data[node] = root

    def union(self, p, q):
        """ add a connection between objects p and q """
        rootp = self._get_root(p)
        rootq = self._get_root(q)
        if self.tree_size[rootp] > self.tree_size[rootq]:
            self.data[q] = rootp
            self.tree_size[rootp] += self.tree_size[rootq]
        else:
            self.data[p] = rootq
            self.tree_size[rootq] += self.tree_size[rootp]

    def connected(self, p, q):
        """ determine if p and q are in the same component """
        return self._get_root(p) == self._get_root(q)

