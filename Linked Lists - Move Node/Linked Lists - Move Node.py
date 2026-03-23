class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """
    Module docstring for function move_node
    """

    new1 = source.next
    new = Node(source.data)
    new.next = dest
    return Context(new1, new)

