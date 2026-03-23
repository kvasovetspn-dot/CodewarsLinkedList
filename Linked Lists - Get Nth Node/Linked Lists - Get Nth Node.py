from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next


def get_nth(node, index):
    """
    Module docstring for function get_nth
    """


    c = 0
    while node:
        if c == index:
            return node
        node = node.next
        c += 1

    raise Exception

