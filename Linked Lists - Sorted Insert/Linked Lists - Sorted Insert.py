""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    """
    Module docstring for function sorted_insert
    """

    if head is None:
        return Node(data)

    if head.data > data:
        new = Node(data)
        new.next = head
        return new

    probe= head
    while probe and probe.next:
        if probe.next.data > data:
            new = probe.next
            probe.next = Node(data)
            probe.next.next = new

            return head

        probe = probe.next

    probe.next = Node(data)
    return head


