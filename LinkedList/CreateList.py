class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def create_linked_list(values: list[int]) -> Node:
    # Node dummyHead = Node (0) # no need to add the type at the beginning
    dummyHead = Node (0)
    curr = dummyHead
    for i in range (len(values)):
        n = Node (values[i])
        curr.next = n
        curr = n
    return dummyHead.next
