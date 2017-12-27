from random import sample, seed
import os
from shutil import rmtree
from union_find_percolation import Percolation, ParseResult, draw_trees
from config import DRAW_TREE, set_graphviz_path

seed(15)

class Percolation_MC(Percolation):
    def __init__(self, n, trials):
        thresholds = []

        for i in range(trials):
            super().__init__(n=n)  # resets simulation
            # http://mathworld.wolfram.com/PercolationThreshold.html (target =	0.592746)
            # hit 0.5934285 percolation threshold n=5 with seed(1220) and trials=3500
            # hit 0.5904724 percolation threshold with n=10 with seed(100) and trials=100000
            # hit 0.5920467 percolation threshold with n=20 with seed(1223) and trials=10000
            # hit 0.5924016 percolation threshold with n=25 with seed(100) and trials=1000 (CLOSEST)
            # hit 0.5931777 percolation threshold with n=30 with seed(7) and trials=1000
            print('Trial', i + 1)
            thresholds.append(self.simulate_percolation())
            if DRAW_TREE:
                if i == trials - 1:
                    set_graphviz_path()
                    path = '../output_files/percolation/n_{n}_t_{t}'.format(n=self.n, t=trials)
                    if os.path.exists(path):
                        rmtree(path)
                    os.mkdir(path)
                    draw_trees(self.data, '../output_files/percolation/n_{n}_t_{t}/MC_test'.format(n=self.n, t=trials))

        print(thresholds)
        print(sum(thresholds)/len(thresholds))

    def simulate_percolation(self):
        num_objects = self.n*self.n
        activation_sequence = sample(range(1, num_objects + 1), num_objects)
        for obj in activation_sequence:  # sequence sampled from list of objects without replacement
            self.activated[obj] = 1
            self.connect_surrounding(obj)
            self.link_top_bottom()
            # self.visualize_activated(self.n)
            # print(self.data)
            # print(self.tree_size)
            parsed = ParseResult(self.data)
            # print(parsed.trees)

            # error check ParseResult
            for root, expected_size in enumerate(self.tree_size):
                if expected_size > 1:
                    actual_size = self._calculate_tree_size(parsed.trees[root])
                    assert expected_size == actual_size, 'data: {data}\ntree_sizes: {sizes}\ntrees: {trees}\nroot: {root}, expected size: {expected_size} actual size: {actual_size}\ntree: {tree}'.format(
                                                    data=self.data, trees=parsed.trees, root=root, sizes=self.tree_size, expected_size=expected_size, actual_size=actual_size, tree=parsed.trees[root])

            if self.connected(self.data[0], self.data[-1]):
                return (activation_sequence.index(obj) + 1)/num_objects

    def visualize_activated(self, n):
        print(self.activated[0])
        for i in range(n):
            print(self.activated[i*n+1:(i+1)*n+1])
        print(self.activated[n*n+1])

    def _calculate_tree_size(self, children):
        size = 0
        for child in children:
            if isinstance(child, tuple):
                size += self._calculate_tree_size(child[1:])
            else:
                size += 1
        return size + 1  # add 1 to account for the parent


Percolation_MC(n=25, trials=1)
