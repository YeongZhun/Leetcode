"""Given the head of a linked list, remove the nth node from the end of the list and return its head."""
#Hint: 2 pointers, but separated by n spacing (.next .next...till n.next), set left pointer starting at dummy.
#Eventually when right pointer hits null, left pointer will be BEFORE the Nth node to be removed.
#Then we just point left pointer .next.next to remove the Nth node.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        #note left = dummy, so that once we moving all the way to the end, left pointer will be BEFORE the Nth node to be deleted
        left = dummy
        right = head

        #This is to set left and right pointer with gap of Nth (right pointer keep moving while we decrement n each time)
        while n > 0 and right:
            right = right.next
            n -= 1
        
        #This is to keep moving both left and right pointer till right hits None/null, then left pointer will be BEFORE the Nth node to be deleted
        while right:
            left=  left.next
            right = right.next
        
        #Delete
        #Finally, just set left pointer to .next.next so that it will point to AFTER the Nth node. Then Nth node will be deleted.
        left.next = left.next.next

        #Lastly, remember there is dummy node in front, and head is dummy.next, so return that.
        return dummy.next

#Time complexity: O(n), iterate through array at most twice only
#Space complexity: O(1), 2 pointers only, no extra memory needed.