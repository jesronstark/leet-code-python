

















# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # Dummy nodes to start the less and greater partitions
        less_head = ListNode(0)
        greater_head = ListNode(0)
        
        # Pointers to build the two partitions
        less = less_head
        greater = greater_head
        
        # Traverse the original list
        current = head
        while current:
            if current.val < x:
                # Append to the less partition
                less.next = current
                less = less.next
            else:
                # Append to the greater partition
                greater.next = current
                greater = greater.next
            current = current.next
        
        # Connect the two partitions
        greater.next = None  # Important to avoid cycle in linked list
        less.next = greater_head.next
        
        # The head of the new list is the next node after less_head
        return less_head.next
