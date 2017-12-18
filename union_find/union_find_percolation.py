import pydotplus as pydot
from math import ceil
from union_find import UF
from config import DRAW_TREE, set_graphviz_path


class Percolation(UF):
    def __init__(self, inputPath=None, n=0):
        self.n = n
        if inputPath:
            self.n, self.succeeds, on_objects = self.read_input(inputPath)

        num_objects = self.n ** 2
        self.data = [i for i in range(num_objects + 2)]  # save 0 index for first node
        self.tree_size = [1 for _ in range(num_objects + 2)]
        self.activated = [0 for _ in range(num_objects)]
        self.activated.insert(0, 1)
        self.activated.append(1)

        if inputPath:
            for pair in on_objects:
                self.activated[(pair[0] - 1) + (pair[1] - 1) * self.n + 1] = 1

            self.link_top_bottom()

            for idx in range(1, len(self.data) - 1):
                if bool(self.activated[idx]):
                    self.connect_surrounding(idx)

            if self.connected(self.data[0], self.data[-1]):
                print('Percolation succeeded')
            else:
                print('Percolation failed')

    @staticmethod
    def read_input(filePath):
        with open(filePath) as inp:
            n = int(inp.readline())
            perlocates = bool(int(inp.readline()))
            on_objects = [[int(coord) for coord in obj.strip('\n').split(' ')] for obj in inp.readlines()]

            return n, perlocates, on_objects

    def link_top_bottom(self):
        for i in range(1, self.n + 1):
            if bool(self.activated[i]):
                if self.get_root(self.data[i]) != self.get_root(self.data[0]):
                    self.union(self.data[i], self.data[0])

        for i in range(len(self.data) - self.n - 1, len(self.data) - 1):
            if bool(self.activated[i]):
                if self.get_root(self.data[i]) != self.get_root(len(self.data) - 1):
                    self.union(self.data[i], len(self.data) - 1)

    def connect_surrounding(self, idx):
        def connect_vertical(idx, delta):
            if bool(self.activated[idx+delta]):
                if self.get_root(self.data[idx+delta]) != self.get_root(self.data[idx]):
                    self.union(self.data[idx], self.data[idx+delta])

        def connect_horizontal(idx, idx_row, delta):
            # check to see if object exists on left & right, connect to it if it is also activated
            if idx + delta >= 0:
                if bool(self.activated[idx + delta]) and ceil((idx + delta) / self.n) == idx_row:
                    if self.get_root(self.data[idx + delta]) != self.get_root(self.data[idx]):
                        # to prevent calling union if there is already connection (would mistakenly increase tree_size)
                        self.union(self.data[idx], self.data[idx + delta])

        idx_row = ceil(idx/self.n)
        if idx-1 >= 0:
            connect_horizontal(idx, idx_row, -1)
        if idx+1 <= len(self.data) - 1:
            connect_horizontal(idx, idx_row, 1)
        if idx-self.n >= 0:
            connect_vertical(idx, -self.n)
        if idx+self.n <= len(self.data) - 1:
            connect_vertical(idx, self.n)


class ParseResult:
    def __init__(self, data):
        self.data = data
        self.trees = {}
        self.get_all_trees()

    def get_all_trees(self):
        for idx, parent in enumerate(self.data):
            if parent != idx:
                if parent not in self.trees.keys():
                    self.trees[parent] = set()
        
        for idx in range(len(self.data)):
            if self.data[idx] in self.trees.keys() and self.data[idx] != idx:
                self.trees[self.data[idx]].add(idx)

        self._aggregate()


    def _aggregate(self):
        while True:
            subtrees_found = False
            for root in set(self.trees.keys()):
                subtrees = self.trees[root].intersection(set(self.trees.keys()))
                for subtree in subtrees:
                    if not self._verify_updated(subtree):
                        continue
                    self.trees[root].remove(subtree)
                    self.trees[root].add((subtree,) + tuple(self.trees[subtree]))
                    # make subtree parent first element of the tuple
                if subtrees:
                    subtrees_found = True
                    continue
            if not subtrees_found:  # if for loop was never broken
                break

    def _verify_updated(self, subtree):
        for element in self.trees[subtree]:
            if isinstance(element, tuple):
                if not self._verify_updated(element[0]):
                    return False
            elif element in self.trees.keys():
                return False
        return True


class DrawTree:
    def __init__(self, root, children, outputPath):
        self.graph = pydot.Dot(graph_type='digraph')
        self.add_edges(root, children)
        self.graph.write_png('{path}_root_{root}.png'.format(path=outputPath, root=root))

    def add_edges(self, parent, children):
        for child in children:
            if isinstance(child, tuple):
                self.graph.add_edge(pydot.Edge(parent, child[0]))
                self.add_edges(child[0], child[1:])  # first item of tuple is root of subtree
            else:
                self.graph.add_edge(pydot.Edge(parent, child))

# TODO document this


def draw_trees(data, name):
    set_graphviz_path()
    parsed = ParseResult(data)
    for num, tree in enumerate(parsed.trees.keys()):
        DrawTree(tree, parsed.trees[tree], name)

if __name__ == '__main__':
    fileName = 'input4_fails'
    testPath = '../test_algorithms/TestUnionFind/test_percolation/{}.txt'.format(fileName)
    result = Percolation(testPath)

    if DRAW_TREE:
        outputPath = '../output_files/percolation/{}'.format(fileName)
        draw_trees(result.data, outputPath)
