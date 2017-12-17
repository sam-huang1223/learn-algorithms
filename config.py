import os

DRAW_TREE = True  # this requires following the pydot installation instructions in the README
GRAPHVIZ_BIN_PATH = 'C:/Program Files (x86)/Graphviz2.38/bin/'


def set_graphviz_path():
    os.environ["PATH"] += os.pathsep + GRAPHVIZ_BIN_PATH
