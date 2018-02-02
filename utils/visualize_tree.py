"""
DrawTree input format:
root = root node
children = set of {child 1, child 2, (child 3, child 3 - child 1, child 3 - child 2)...}
node_attributes = list of [NodeAttributes object 1, NodeAttributes object 2...]
"""

import pydotplus as pydot
from itertools import zip_longest

from config import set_graphviz_path


class PercolationParseResult:
    """Used for the union_find percolation algorithms"""
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


class NodeAttributes:  # can be replaced with a dataclass from Python 3.7
    def __init__(self, edge_color):
        self.edge_color = edge_color


class DrawTree:
    def __init__(self, root, children, node_attributes, outputPath):
        self.graph = pydot.Dot(graph_type='digraph')
        self.add_edges(root, children, node_attributes)
        self.graph.write_png('{path}_root_{root}.png'.format(path=outputPath, root=root))

    def add_edges(self, parent, children, node_attributes):
        for child, attributes in zip_longest(children, node_attributes):
            if isinstance(child, tuple):
                color = attributes[0].edge_color if isinstance(attributes, tuple) else 'black'
                self.graph.add_edge(pydot.Edge(parent, child[0], color=color))
                self.add_edges(child[0], child[1:], attributes[1:] if attributes else ())  # first item of tuple is root of subtree
            else:
                color = attributes.edge_color if attributes else 'black'
                self.graph.add_edge(pydot.Edge(parent, child, color=color))


def draw_trees(trees, node_attributes=(), outputPath='tree'):
    set_graphviz_path()
    for num, tree in enumerate(trees.keys()):
        DrawTree(tree, trees[tree], node_attributes, outputPath)
