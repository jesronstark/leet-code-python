class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)  # Dummy node to serve as the new list's head
        tail = dummy  # Tail pointer for the new list
        current = head
        
        while current:
            if current.next and current.val == current.next.val:
                # Skip all nodes with the current value
                while current.next and current.val == current.next.val:
                    current = current.next
            else:
                # Append the current node to the new list
                tail.next = ListNode(current.val)
                tail = tail.next
            current = current.next
        
        return dummy.next
