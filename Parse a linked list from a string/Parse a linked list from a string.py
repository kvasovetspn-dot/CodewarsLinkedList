"""
Module docstring for Parse a linked list from a string
"""

from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    """
    Module docstring for function linked_list_from_string
    """

    if list_repr == 'None':
        return None

    lst = list_repr.split(" -> ")

    head = Node(int(lst[0]))
    probe = head
    for el in lst[1:]:
        if el != 'None':
            el = int(el)
            probe.next = Node(el)

            probe = probe.next

    return head

