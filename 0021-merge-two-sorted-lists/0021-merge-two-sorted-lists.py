# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        # Create a dummy node to serve as the start of the merged list
        dummy = ListNode(0)
        current = dummy
        
        # Traverse both lists and attach the smaller value node to current
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
        # Attach the remaining elements if one list is longer than the other
        current.next = list1 if list1 else list2
        
        return dummy.next
        