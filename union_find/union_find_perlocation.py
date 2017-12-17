import pydotplus as pydot
from collections import Counter

from union_find import UF
from config import DRAW_TREE, set_graphviz_path


class Perlocation(UF):
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

        assert self.connected(self.data[0], self.data[-1]) == succeeds, "Perlocation result does not match file input"
        if succeeds:
            print('Perlocation confirmed to be successful')
        else:
            print('Perlocation confirmed to fail')

    @staticmethod
    def read_input(fileName):
        with open('../testing_files/perlocation/{file}'.format(file=fileName)) as inp:
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

    @staticmethod
    def _aggregate(trees):
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
        self.graph = pydot.Dot(graph_type='digraph')
        self.add_edges(root, children)
        self.graph.write_png('../output_files/perlocation/{}_root{}.png'.format(outputName,root))

    def add_edges(self, parent, children):
        for child in children:
            if isinstance(child, tuple):
                self.graph.add_edge(pydot.Edge(parent, child[0]))
                self.add_edges(child[0], child[1:])  # first item of tuple is root of subtree
            else:
                self.graph.add_edge(pydot.Edge(parent, child))

# TODO document this

if __name__ == '__main__':
    testCase = 'input4_fails'
    result = Perlocation('{}.txt'.format(testCase))
    parsed = ParseResult(result.data)

    if DRAW_TREE:
        set_graphviz_path()
        for num, tree in enumerate(parsed.trees.keys()):
            DrawTree(tree, parsed.trees[tree], testCase)