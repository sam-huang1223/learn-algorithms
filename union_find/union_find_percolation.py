from math import ceil
from union_find import UF
from config import DRAW_TREE
from utils.visualize_tree import draw_trees, PercolationParseResult

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


if __name__ == '__main__':
    fileName = 'input4_fails'
    testPath = '../test_algorithms/TestUnionFind/test_percolation/{}.txt'.format(fileName)
    result = Percolation(testPath)

    if DRAW_TREE:
        outputPath = '../output_files/percolation/{}'.format(fileName)
        parsed = PercolationParseResult(result.data)
        draw_trees(parsed.trees, outputPath=outputPath)
