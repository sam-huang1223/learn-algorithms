import pydotplus as pydot
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'


class OnNode(pydot.Node):
    def __init__(self, label):
        super().__init__(label, style="filled", shape="circle", fillcolor="black", fontcolor='white')


class OffNode(pydot.Node):
    def __init__(self, label):
        super().__init__(label, style="filled", shape="circle", fillcolor="white", fontcolor='black')


class DrawGraph:
    def __init__(self, inputName):
        n, on_objects = self.read_input('{}.txt'.format(inputName))
        self.graph = pydot.Dot(graph_type='graph', label=inputName)
        self.input = [0 for _ in range(n * n)]

        for pair in on_objects:
            self.input[(pair[0]-1) + (pair[1]-1)*n] = 1

        self.graph.add_node(OnNode(0))
        self.graph.add_node(OnNode(len(self.input) + 1))

        for node_num, node_state in enumerate(self.input):
            if bool(node_state):
                node = OnNode(node_num + 1)
            else:
                node = OffNode(node_num + 1)
            self.graph.add_node(node)

        for node_num in range(1, len(self.input) + 1):
            self.add_edges_horizontal(self.graph.get_node(str(node_num))[0], node_num, n)
            self.add_edges_vertical(self.graph.get_node(str(node_num))[0], node_num, n)

        # TODO hand-draw and take picture to compare/contrast with algo generated version

        self.graph.write_png('{}.png'.format(inputName))

    @staticmethod
    def read_input(fileName):
        with open(fileName) as inp:
            n = int(inp.readline())
            _ = inp.readline()
            on_objects = [[int(coord) for coord in obj.strip('\n').split(' ')] for obj in inp.readlines()]
            return n, on_objects

    def add_edges_horizontal(self, node, node_num, n):
        if node_num-1 > 0:
            self.graph.add_edge(pydot.Edge(node, self.graph.get_node(str(node_num-1))[0]))
        if node_num+1 <= len(self.input) - 1:
            self.graph.add_edge(pydot.Edge(node, self.graph.get_node(str(node_num+1))[0]))

    def add_edges_vertical(self, node, node_num, n):
        if node_num-n > 0:
            self.graph.add_edge(pydot.Edge(node, self.graph.get_node(str(node_num-n))[0]))
        if node_num+n <= len(self.input) - 1:
            self.graph.add_edge(pydot.Edge(node, self.graph.get_node(str(node_num+n))[0]))

DrawGraph('input4_succeeds')