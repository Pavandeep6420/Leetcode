# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        # Create a dummy node to point to the head of the list
        dummy = ListNode(0, head)
        prev = dummy
        
        while prev.next and prev.next.next:
            # Identify the two nodes to swap
            first = prev.next
            second = prev.next.next
            
            # Perform the swap
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move the prev pointer two nodes forward for the next pair
            prev = first
            
        return dummy.next
        