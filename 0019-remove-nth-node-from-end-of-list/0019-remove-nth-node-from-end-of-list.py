# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # Create a dummy node to handle edge cases like removing the head node
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # Move the right pointer n steps ahead
        for _ in range(n):
            right = right.next
            
        # Move both pointers until right reaches the end of the list
        while right:
            left = left.next
            right = right.next
            
        # Delete the target node by skipping it
        left.next = left.next.next
        
        return dummy.next
        