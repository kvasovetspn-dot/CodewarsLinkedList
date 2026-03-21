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


n1 = Node(2)
n1.next = Node(3)

p1 = reverse(n1)
while p1:
    print(p1.data)
    p1 = p1.next

#def recursive_f(st):
    #     """
    #     Module docstring for function recursive_f
    #     """

    #     return st.next

    # new = None
    # probe = head
    # while probe:
    #     if not probe or probe and not probe.next:
    #         if new and probe:
    #             new.next = probe
    #         else:
    #             new = probe
    #         return new
    #     st = recursive_f(head)
    #     if new:
    #         new.next = Node(st)
    #     else:
    #         new = Node(st)
