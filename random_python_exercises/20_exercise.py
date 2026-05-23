from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val;
        self.next = next;

def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    current_node: ListNode | None = head

    while current_node is not None and current_node.next is not None:
        next_position: ListNode | None = current_node.next

        if next_position.val == current_node.val:
            current_node.next = next_position.next
        else:
            current_node = next_position
        
    return head

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)

def print_result(head: Optional[ListNode]):
    current_node = head
    while current_node:
        print(current_node.val, end=" -> ")
        current_node = current_node.next

print(print_result(delete_duplicates(head))) 