from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next

def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    sum_list: ListNode = ListNode()
    current_node: ListNode = sum_list
    carry: int = 0

    while l1 or l2 or carry:
        value_one: int = l1.val if l1 else 0
        value_two: int = l2.val if l2 else 0
        total: int = value_one + value_two + carry

        if total >= 10:
            total -= 10
            carry = 1
        else:
            carry = 0
        
        current_node.next = ListNode(total)
        current_node = current_node.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return sum_list.next