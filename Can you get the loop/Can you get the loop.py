class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def loop_size(node):
    """
    Module docstring for function loop_size
    """

    fast = node
    slow = node

    while fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    fast = fast.next
    c = 1
    while fast != slow:
        fast = fast.next
        c += 1

    return c

