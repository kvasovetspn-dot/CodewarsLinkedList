"""
Module docstring for Convert a linked list to a string
"""

class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    """
    Module docstring for function stringify
    """

    if not node:
        return 'None'
    nodes_str = []
    while node:
        nodes_str.append(str(node.data))
        node = node.next
    return ' -> '.join(nodes_str) + ' -> None'

