from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    reversed_list_node: ListNode | None = None
    current_node: ListNode | None = head

    while current_node is not None:
        next_position: ListNode | None = current_node.next # 2 - 3 - 4 - 5 - null
        current_node.next = reversed_list_node # null - 1 - 2 - 3 - 4
        reversed_list_node = current_node # 1 - 2 - 3 - 4 - 5
        current_node = next_position # 2 - 3 - 4 - 5 - null

    return reversed_list_node

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

def print_list(head: Optional[ListNode]):
    current= head
    while current:
        print(current.val, end=" -> ")
        current = current.next

print_list(reverse_list(head))