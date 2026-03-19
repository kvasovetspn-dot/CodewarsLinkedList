from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def push(head, data):
    """
    Module docstring for function push
    """

    new = Node(data)
    new.next = head
    return new

def build_one_two_three():
    """
    Module docstring for function build_one_two_three
    """

    lst = Node(1)
    lst.next = Node(2)
    lst.next.next = Node(3)
    return lst

