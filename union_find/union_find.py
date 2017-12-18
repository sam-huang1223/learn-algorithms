class UF:
    def __init__(self, n):
        """ Initialize union-find data structure with N objects (0 to N-1) """
        self.data = [i for i in range(n)]
        self.tree_size = [1 for i in range(n)]

    def get_root(self, value):
        """ Finds the root of any given object """
        while self.data[value] != value:
            value = self.data[value]
        return value

    def visualize_activated(self, n):
        print(self.activated[0])
        for i in range(n):
            print(self.activated[i*n+1:(i+1)*n+1])
        print(self.activated[n*n+1])

    def union(self, p, q):
        """ add a connection between objects p and q """
        rootp = self.get_root(p)
        rootq = self.get_root(q)
        if self.tree_size[rootp] > self.tree_size[rootq]:
            self.data[rootq] = rootp
            if rootp != rootq:  # do not duplicate combining tree sizes if already in the same tree
                self.tree_size[rootp] += self.tree_size[rootq]
            else:
                self.tree_size[rootp] += 1  # in that case, just adding 1 more node to the tree
        else:
            self.data[rootp] = rootq
            if rootq != rootp:
                self.tree_size[rootq] += self.tree_size[rootp]
            else:
                self.tree_size[rootq] += 1

    def connected(self, p, q):
        """ determine if p and q are in the same component """
        return self.get_root(p) == self.get_root(q)

