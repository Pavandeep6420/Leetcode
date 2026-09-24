class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curr = root
        
        while curr:
            dummy = Node(0)
            tail = dummy
            
            # Traverse the current level using 'next' pointers
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next
            
            # Move to the start of the next level
            curr = dummy.next
            
        return root
        