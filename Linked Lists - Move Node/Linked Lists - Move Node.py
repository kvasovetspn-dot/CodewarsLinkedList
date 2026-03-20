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

source = Node(1)
source.next = Node(2)
source.next.next = Node(3)
dest = Node(4)
dest.next = Node(5)
dest.next.next = Node(6)
while move_node(source, dest).source:
    print(move_node(source, dest).source)
    move_node(source, dest).source = move_node(source, dest).source.next
print(move_node(source, dest).source)
print(move_node(source, dest).dest)
