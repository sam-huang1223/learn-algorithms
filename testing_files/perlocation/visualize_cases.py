import pydot_ng as pydot
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

class DrawGraph:
    def __init__(self, inputName):
        n, succeeds, on_objects = self.read_input('{}.txt'.format(inputName))
        self.graph = pydot.Dot(graph_type='graph')

        # TODO this

        #self.add_edges(root, children)
        self.graph.write_png('{}.png'.format(inputName))

    @staticmethod
    def read_input(fileName):
        with open(fileName) as inp:
            n = int(inp.readline())
            perlocates = bool(int(inp.readline()))
            on_objects = [[int(coord) for coord in obj.strip('\n').split(' ')] for obj in inp.readlines()]
            return n, perlocates, on_objects

    def add_edges(self, parent, children):
        for child in children:
            if isinstance(child, tuple):
                self.graph.add_edge(pydot.Edge(parent, child[0]))
                self.add_edges(child[0], child[1:])  # first item of tuple is root of subtree
            else:
                self.graph.add_edge(pydot.Edge(parent, child))

DrawGraph('input4_succeeds')