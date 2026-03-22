from preloaded import Node

def swap_pairs(head):
    """
    Module docstring for function swap_pairs
    """

    if not head or not head.next:
        return head


    d = Node()
    d.next = head
    prev = d
    while prev and prev.next and prev.next.next:

        first= prev.next
        second = prev.next.next

        prev.next = second

        first.next = second.next

        second.next = first

        prev = first


    return d.next
