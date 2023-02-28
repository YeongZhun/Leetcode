"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself."""
#This problem need to imagine doing addition on the table manually. e.g. 8+7 = 15, but it will be 5, then carry 10 over to next number, etc


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        cur = dummy

        carry = 0
        #why 'or carry'? This is to ensure cases e.g. 8+7=15, we put 5, carry the 10 (or rather 1) over, but without 'or carry',
        #the loop will just stop, since l1 and l2 both have 1 length only. Thus we need to  put 'or carry', so that if there is actually a carry,
        #we need to carry on with the loop. v1 and v2 will be 0, and val = carry, which will be evaluated.
        while l1 or l2 or carry:
            #These 2 lines is for the case where the size of v1 and v2 is not equal. e.g. 87 + 100. The smaller number will have an extra 0, e.g. 087 and 100.
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            #new digit
            val = v1 + v2 + carry
            #note: if val is < 10, it will always be 0, as they are less than 10.
            carry = val // 10
            #note: if val is < 10, it will always return val back, as it cannot be divided by 10, remainder will be exactly same value.
            val = val % 10
            cur.next = ListNode(val)

            #update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

#Time Complexity: O(max(m,n)) , maximum of list1 or list2
#Space Complexity: O(max(m,n)), maximum of list1 or list2
