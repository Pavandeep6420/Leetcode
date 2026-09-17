# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if not head or left == right:
            return head
            
        # Create a dummy node to handle edge cases like reversing from position 1
        dummy = ListNode(0, head)
        prev = dummy
        
        # 1. Move 'prev' to the node just before the 'left' position
        for _ in range(left - 1):
            prev = prev.next
            
        # 2. 'current' points to the first node of the sublist to be reversed
        current = prev.next
        
        # 3. Reverse the sublist from 'left' to 'right' in-place
        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
            
        return dummy.next