class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def delete_node(head: Node, value: int) -> Node:
    if head is None:
        return head

    if head.val == value:
        return head.next

    curr = head 
    while curr and curr.next:
        if curr.next.val == value:
            curr.next = curr.next.next
            return head 
        curr = curr.next    
    return head
