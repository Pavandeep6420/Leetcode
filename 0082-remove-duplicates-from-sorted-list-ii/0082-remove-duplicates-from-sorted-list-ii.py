# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        # Create a dummy node to handle edge cases where the head itself has duplicates
        dummy = ListNode(0, head)
        prev = dummy
        
        current = head
        while current:
            # Check if current node has duplicates ahead
            if current.next and current.val == current.next.val:
                # Skip all nodes with the same value
                while current.next and current.val == current.next.val:
                    current = current.next
                # Connect prev to the node after the last duplicate
                prev.next = current.next
            else:
                # No duplicates, move prev forward
                prev = prev.next
                
            current = current.next
            
        return dummy.next