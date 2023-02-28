"""You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed."""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        #find middle of the linked list to split (slow will finally be at END of first list. Basically slow.next will be START of second list (not reversed yet))
        slow, fast = head, head.next
        #while fast is not null and has not reached the end of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #Reverse the second list
        second = slow.next
        #We set slow.next to None to break off the link, to officially separate the first and second linked list.
        slow.next = None 
        #prev is always initialized to None/null first
        prev = None
        while second:
            #temp will keep a temporary variable of the original second.next, as in the next line, prev will be set as the value of second.next
            temp = second.next
            #reverse the link by setting second.next to be prev
            second.next = prev
            #Now that it is reversed, we set the current second to be prev
            prev = second
            #and update the original second.next (now stored as temp) to be current second (basically we move them to the right and repeat the while loop)
            second = temp
        
        #second list has been reversed now.
        #merge two halfs 1->2->3 and 4->5 (5->4 after reverse) become 1->5->2->4->3 alternate merge
        #Note, second is set to prev, because in while loop above, it stops when second is null (which is original second.next stored in temp)
        #Thus, prev is the last node, which is now the new HEAD of the reversed second list.
        #Which is what we want to set second as here.
        first, second = head, prev

        #keep looping as long as one of the list is not None/null. But second could be shorter than first (if original list is odd list), so set second as condition
        while second:
            #Same thing above, we store the .next values of both list first, to use it later
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            #First list = 1->2->3 and Second list = 5->4, We are setting new first from 1 to 2, and new second from 5 to 4, etc..
            first, second = temp1, temp2

#Time complexity: O(n), iterate through the list at most twice
#Space complexity: O(1), no extra memory needed