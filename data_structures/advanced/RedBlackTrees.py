from utils.visualize_tree import draw_trees, NodeAttributes

a = ()

# test ability to draw trees (for error identification purposes)
draw_trees({0: (1,(2, 3))}, node_attributes=[
    NodeAttributes(edge_color='yellow'), (NodeAttributes(edge_color='pink'), NodeAttributes(edge_color='green'))
])
