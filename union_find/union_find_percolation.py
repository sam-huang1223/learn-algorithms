import pydotplus as pydot
from math import ceil
from union_find import UF
from config import DRAW_TREE, set_graphviz_path


class Percolation(UF):
    def __init__(self, inputFile=None, n=0):
        if inputFile:
            n, succeeds, on_objects = self.read_input(inputFile)

        self.data = [i for i in range(n * n + 2)]  # save 0 index for first node
        self.tree_size = [1 for _ in range(n * n + 2)]
        self.activated = [0 for _ in range(n * n)]
        self.activated.insert(0, 1)
        self.activated.append(1)

        if inputFile:
            for pair in on_objects:
                self.activated[(pair[0] - 1) + (pair[1] - 1) * n + 1] = 1

            self.link_top_bottom(n)

            for idx in range(1, len(self.data) - 1):
                if bool(self.activated[idx]):
                    self.connect_surrounding(idx, n)

            assert self.connected(self.data[0], self.data[-1]) == succeeds, "Percolation result does not match file input"
            if succeeds:
                print('Percolation confirmed to be successful')
            else:
                print('Percolation confirmed to fail')

    @staticmethod
    def read_input(fileName):
        with open('../testing_files/percolation/{file}'.format(file=fileName)) as inp:
            n = int(inp.readline())
            perlocates = bool(int(inp.readline()))
            on_objects = [[int(coord) for coord in obj.strip('\n').split(' ')] for obj in inp.readlines()]

            return n, perlocates, on_objects

    def link_top_bottom(self, n):
        for i in range(1, n + 1):
            if bool(self.activated[i]):
                if self.get_root(self.data[i]) != self.get_root(self.data[0]):
                    self.union(self.data[i], self.data[0])

        for i in range(len(self.data) - n - 1, len(self.data) - 1):
            if bool(self.activated[i]):
                if self.get_root(self.data[i]) != self.get_root(len(self.data) - 1):
                    self.union(self.data[i], len(self.data) - 1)

    def connect_surrounding(self, idx, n):
        def connect_vertical():
            pass

        def connect_horizontal():
            pass

        idx_row = ceil(idx/n)
        # check to see if [left] object exists, connect to it if it is also on
        # TODO make if statements into a function
        if idx-1 >= 0:
            if bool(self.activated[idx-1]) and ceil((idx-1)/n) == idx_row:
                if self.get_root(self.data[idx-1]) != self.get_root(self.data[idx]):
                    # to prevent calling union if there is already connection (^^ tree_size)
                    self.union(self.data[idx], self.data[idx-1])
        if idx+1 <= len(self.data) - 1:
            if bool(self.activated[idx+1]) and ceil((idx+1)/n) == idx_row:
                if self.get_root(self.data[idx+1]) != self.get_root(self.data[idx]):
                    self.union(self.data[idx], self.data[idx+1])
        if idx-n >= 0:
            if bool(self.activated[idx-n]):
                if self.get_root(self.data[idx-n]) != self.get_root(self.data[idx]):
                    self.union(self.data[idx], self.data[idx-n])
        if idx+n <= len(self.data) - 1:
            if bool(self.activated[idx+n]):
                if self.get_root(self.data[idx+n]) != self.get_root(self.data[idx]):
                    self.union(self.data[idx], self.data[idx+n])


class ParseResult():
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
    def __init__(self, root, children, outputName):
        self.graph = pydot.Dot(graph_type='digraph')
        self.add_edges(root, children)
        self.graph.write_png('../output_files/percolation/{}_root{}.png'.format(outputName,root))

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
    testCase = 'input4_fails'
    result = Percolation('{}.txt'.format(testCase))

    if DRAW_TREE:
        draw_trees(result.data, testCase)
