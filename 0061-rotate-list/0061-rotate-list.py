# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Handle edge cases: empty list, single node, or no rotation needed
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find the length of the linked list and get the tail node
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
            
        # Step 2: Optimize k if it's greater than the length
        k = k % length
        if k == 0:
            return head
            
        # Step 3: Connect the tail to the head to form a circular list
        tail.next = head
        
        # Step 4: Find the new tail position (length - k - 1 steps from the head)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
            
        # Step 5: Break the circle to form the new rotated list
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
        