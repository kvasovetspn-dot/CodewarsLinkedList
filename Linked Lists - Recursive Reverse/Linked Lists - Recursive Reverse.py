class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    """
    Module docstring for function reverse
    """

    if not head or not head.next:
        return head

    rev = reverse(head.next)

    head.next.next = head
    head.next = None

    return rev


