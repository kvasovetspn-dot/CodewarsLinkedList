class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    """
    Module docstring for function remove_duplicates
    """

    if not head:
        return None



    probe = head

    while probe and probe.next:
        if probe.data == probe.next.data:

            probe.next = probe.next.next
        else:
            probe = probe.next



    return head

n1 = Node(1)
n1.next = Node(1)
n1.next.next = Node(3)
n1.next.next.next = Node(3)
n1.next.next.next.next = Node(3)
# n1.next.next.next.next.next = Node(4)
# n1.next.next.next.next.next.next = Node(5)
# n1.next.next.next.next.next.next.next = Node(5)

n1 = remove_duplicates(n1)

while n1:
    print(n1.data)
    n1 = n1.next


n2 = remove_duplicates(None)
print(n2)
while n2:
    print(n2.data)
    n2 = n2.next
