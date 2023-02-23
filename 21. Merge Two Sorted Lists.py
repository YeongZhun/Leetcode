"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
#Hint: Put a pointer at each list, compare them, put lowest value into final list. Shift pointer to next value and repeat. 
#If any list pointer reach the end, means we can just add the remaining other list to the final list.

#Definition for singly-linked list.
# Linked List Node
class Node():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
# Create & Handle List operations
class LinkedList:
    def __init__(self):
        self.head = None
 
    # Method to display the list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
 
    # Method to add element to list
    def addToList(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
 
        last = self.head
        while last.next:
            last = last.next
 
        last.next = newNode

class Solution():
    def mergeTwoLists(self, list1head: Node, list2head: Node) -> LinkedList:
        #setting a dummy at first to prevent Edge cases and getting errors
        dummy = Node()
        tail = dummy

        #Do condition only while list1head and list2head is not empty. If it is, proceed to next step (adding remaining leftover list1head/list2head to the final result)
        while list1head and list2head:
            #if list1headhead < list2head, add current value of list1head (the lowest) to the final list, then move list1head pointer to next value.
            if list1head.val < list2head.val:
                tail.next = list1head
                list1head = list1head.next
            #otherwise list2head > list1head, same logic above
            else:
                tail.next = list2head
                list2head = list2head.next
            #regardless whether list1head or list2head value is added, we have to shift pointer of final list to the next possible value so that while loop can iterate and add it there.
            tail = tail.next
        
        #Once while loop is over, it means either both list1head and list2head are empty, or ONE of the list is empty now, but there is a list that still has some remaining values.
        #Thus, we put the list with remaining values and add on to the final list result, then it will be done.
        if list1head:
            tail.next = list1head
        elif list2head:
            tail.next = list2head
        
        print("Yay")
        return dummy.next

test_solution = Solution()
list1 = LinkedList()
list2 = LinkedList()

list1.addToList(1)
list1.addToList(3)
list1.addToList(5)
list1.addToList(7)
list2.addToList(2)
list2.addToList(4)
list2.addToList(6)
list2.addToList(8)
list2.addToList(10)

combined_list = LinkedList()
combined_list.head = test_solution.mergeTwoLists(list1.head, list2.head)
LinkedList.printList(combined_list)

#Time Complexity: O(m+n) , where m is list 1, n is list 2
#Space Complexity: O(1), we are just shifting the pointers