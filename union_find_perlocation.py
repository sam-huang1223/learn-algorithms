import pydot_ng as pydot
from collections import Counter


class Perlocation:
    def __init__(self, inputFile):
        n, succeeds, on_objects = self.read_input(inputFile)
        self.input = [0 for _ in range(n*n)]
        self.data = [i for i in range(1, n*n + 1)]  # save 0 index for first node
        self.tree_size = [1 for _ in range(n*n + 2)]

        for pair in on_objects:
            self.input[(pair[0]-1) + (pair[1]-1)*n] = 1
        self.input.insert(0, 1)
        self.input.append(1)
        
        self.data.insert(0, 0)  # first node connecting all nodes in top row
        for i in range(1, n + 1):
            if bool(self.input[i]):
                self.union(self.data[i], self.data[0])

        self.data.append(len(self.data))  # last node connecting all nodes in bottom row
        for i in range(len(self.data) - n - 1, len(self.data) - 1):
            if bool(self.input[i]):
                self.union(self.data[i], len(self.data) - 1)

        for idx in range(len(self.data)):
            if bool(self.input[idx]):
                self.connect_surrounding(idx, n)

        self.perlocated = self.connected(self.data[0], self.data[-1])
        assert self.perlocated == succeeds, "Perlocation result does not match file input"
        
    @staticmethod
    def read_input(fileName):
        with open('./testing_files/perlocation/{file}'.format(file=fileName)) as inp:
            n = int(inp.readline())
            perlocates = bool(int(inp.readline()))
            on_objects = [[int(coord) for coord in obj.strip('\n').split(' ')] for obj in inp.readlines()]

            return n, perlocates, on_objects

    def connect_surrounding(self, idx, n):
        # check to see if [left] object exists, connect to it if it is also on
        if idx-1 >= 0:
            if bool(self.input[idx-1]):
                self.union(self.data[idx], self.data[idx-1])
        if idx+1 <= len(self.data) - 1:
            if bool(self.input[idx+1]):
                self.union(self.data[idx], self.data[idx+1])
        if idx-n >= 0:
            if bool(self.input[idx-n]):
                self.union(self.data[idx], self.data[idx-n])
        if idx+n <= len(self.data) - 1:
            if bool(self.input[idx+n]):
                self.union(self.data[idx], self.data[idx+n])

    def compress_path(self, node, root):
        while self.data[node] != node:
            node = self.data[node]
            self.data[node] = root

    def union(self, p, q):
        ''' add a connection between objects p and q '''
        rootp = self._get_root(p)
        rootq = self._get_root(q)
        if self.tree_size[rootp] > self.tree_size[rootq]:
            self.data[q] = rootp
            self.tree_size[rootp] += self.tree_size[rootq]
        else:
            self.data[p] = rootq
            self.tree_size[rootq] += self.tree_size[rootp]
    
    def _get_root(self, value):
        ''' Finds the root of any given object '''
        initial_node = value
        while self.data[value] != value:
            value = self.data[value]
        self.compress_path(initial_node, value)
        return value

    def connected(self, p, q):
        ''' determine if p and q are in the same component '''
        return self._get_root(p) == self._get_root(q)


class ParseResult:
    def __init__(self, data):
        self.data = data
        self.trees = self.get_all_trees()

    def get_all_trees(self):
        trees = {}
        for root, count in Counter(self.data).items():
            if count > 1:  # only take trees with size > 1
                trees[root] = set()
        
        for idx in range(len(self.data)):
            if self.data[idx] in trees.keys() and self.data[idx] != idx:
                trees[self.data[idx]].add(idx)

        return self._aggregate(trees)

    def _aggregate(self, trees):
        while True:
            roots = set(trees.keys())
            for root in roots:
                subtrees = trees[root].intersection(roots)
                for subtree in subtrees:
                    trees[root].remove(subtree)
                    trees[root].add((subtree,) + tuple(trees[subtree]))  # make subtree parent first element of the tuple
                    del trees[subtree]
                if subtrees:
                    break
            else:  # if for loop was never broken
                return trees


class DrawTree:
    def __init__(self, root, children, outputName):
        self.graph = pydot.Dot(graph_type='graph')
        self.add_edges(root, children)
        self.graph.write_png('{}.png'.format(outputName))

    def add_edges(self, parent, children):
        for child in children:
            if isinstance(child, tuple):
                self.graph.add_edge(pydot.Edge(parent, child[0]))
                self.add_edges(child[0], child[1:])  # first item of tuple is root of subtree
            else:
                self.graph.add_edge(pydot.Edge(parent, child))


import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
# TODO move whether to draw to config file (also move GraphViz path to config file)
# TODO document this

testCase = 'input4_succeeds'
result = Perlocation('{}.txt'.format(testCase))
parsed = ParseResult(result.data)
for num, tree in enumerate(parsed.trees.keys()):
    # TODO save trees in separate folder
    # TODO number trees based on root
    DrawTree(tree, parsed.trees[tree], testCase)