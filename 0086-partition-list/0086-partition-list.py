# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        # Create dummy heads for two separate lists: one for values < x, one for values >= x
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        
        less = less_dummy
        greater = greater_dummy
        
        current = head
        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next
            
        # Important: terminate the greater list to prevent cycles
        greater.next = None
        
        # Connect the 'less' partition to the start of the 'greater' partition
        less.next = greater_dummy.next
        
        return less_dummy.next
        