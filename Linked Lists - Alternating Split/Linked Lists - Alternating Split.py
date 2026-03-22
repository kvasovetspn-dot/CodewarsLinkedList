class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    """
    Module docstring for function alternating_split
    """

    if not head or not head.next:
        raise AssertionError

    probe = head
    c = 0
    new = Context(None, None)
    while probe:

        if c % 2 == 0:
            if new.first:

                p = new.first
                while p:
                    if not p.next:

                        p.next = Node(probe.data)
                        break
                    p = p.next


            else:
                new.first = Node(probe.data)
        else:
            if new.second:
                p = new.second
                while p:
                    if not p.next:

                        p.next = Node(probe.data)
                        break
                    p = p.next
            else:
                new.second = Node(probe.data)

        probe = probe.next
        c += 1

    return new

