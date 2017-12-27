class try_node:
    def __init__(self, children):
        # optimization: each node stores number of children
        self.children = children
        self.num_children = len(children)

class tries:
    def __init__(self):
        pass
