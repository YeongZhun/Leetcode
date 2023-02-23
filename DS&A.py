"""
Liner Data Structures
These are the data structures which store the data elements in a sequential manner.

Array: It is a sequential arrangement of data elements paired with the index of the data element.
Linked List: Each data element contains a link to another element, along with the data present in it.
Stack: It is a data structure, which follows only to specific order of operation. LIFO (last in First Out) or FILO(First in Last Out).
Queue: It is similar to Stack, but the order of operation is only FIFO (First In First Out).
Matrix: It is two dimensional data structure in which, the data element is referred by a pair of indices.

Non-Liner Data Structures
These are the data structures in which, there is no sequential linking of data elements. Any pair or group of data elements can be linked to each other and can be accessed without a strict sequence. 

Binary Tree: It is a data structure, where each data element can be connected to maximum two other data elements and it starts with a root node.
Heap: It is a special case of Tree data structure, where the data in the parent node is either strictly greater than/ equal to the child nodes or strictly less than its child nodes.
Hash Table: It is a data structure, which is made of arrays associated with each other using a hash function. It retrieves values using keys rather than, index from a data element.
Graph: It is an arrangement of vertices and nodes, where some of the nodes are connected to each other through links.

Python Specific Data Structures

List: It is similar to array with the exception, that the data elements can be of different data types. You can have both numeric and string data in a python list.
Tuple: Tuples are similar to lists, but they are immutable which means, the values in a tuple cannot be modified they can only be read.
Dictionary: The dictionary contains Key-value pairs as its data elements.

"""
#Types of Search

#Linear Search
#Unsorted
def UnsortedLinearSearch(list, target):
    #Get length of list
    length = len(list)
    #Check every index one by one, if target found, return True, otherwise if whole list cannot find, return False
    for i in range(length):
        if list[i] == target:
            return True
    return False 

Unsortedlist=[4,5,2,8,1,7,3,0]

print(f"Unsorted Linear Search: {UnsortedLinearSearch(Unsortedlist, 5)}")
#Time Complexity: O(n) for worst
#Space Complexity: O(1)

#Sorted
def SortedLinearSearch(list, target):
    #Get length of list
    length = len(list)
    #Check every index one by one, if target found, return True, otherwise if whole list cannot find, return False
    for i in range(length):
        if list[i] == target:
            return True
        #Since list is sorted, if current list[i] number is higher than target, there is no point searching. Confirmed that target does not exist
        elif list[i] > target:
            return False
    return False 

SortedList=[0,1,2,3,4,5,6,7,8,9,10]

print(f"Sorted Linear Search: {SortedLinearSearch(SortedList, 5)}")

#Binary Search
#Only applicable to SORTED sequence. Search in the middle of the sequence every time, cutting away half of the sequence every time, making it more efficient than linear search
def BinarySearch(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:
        #Use // to get floor integer division, as we need it to be integer while using it to index the list. If use /, it will always be a float type.
        mid = (low + high)//2
        if list[mid] == target:
            return True
        #If target is lower than middle values, we will exclude the upper half of the sequence by setting high as mid - 1
        elif target < list[mid]:
            high = mid - 1
        #Else if target is higher than middle values, we will exlude the lower half of the sequence by setting low as mid + 1
        else:
            low = mid + 1
    #If target cannot be found in the whole sequence, return False
    return False
#Time Complexity: O(log2 n)
#At every iteration, can cut down by half
#Space Complexity: O(1)

SortedList2=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(f"Binary Search: {BinarySearch(SortedList2, 13)}")

#Sorting an unsorted sequence the fastest way possible

#Bubble Sort
#Compare the first and second values first. If first > second, swap it. If second > first, move on to next comparison, compare the second and third values, and repeat till the end. 
#At the end, we can be very sure the last value is definitely the largest value. 
#We repeat this process until we are sure every value is sorted. (n-1) times
def BubbleSort(list):
    n = len(list)
    for i in range(n-1):
        #n-1-i because after each iteration of inner loop, we are sure the last value is largest value, thus there is no need to compare. so there is -i .
        for j in range(n - 1 - i):
            #if j > j+1, swap using temp 
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list
#Time Complexity: O(n^2)
#If arrays sorted in descending order, need to compare and swap (n-1)+(n-2)+(n-3)...
#Space Complexity: O(1)

UnsortedBubbleList = [8,1,4,3,7,6,2,5]

print(f"Bubble Sorted list: {BubbleSort(UnsortedBubbleList)}")

#Selection Sort
#Scan through the whole sequence, find the smallest value. Once found, take out the smallest value, place it at the front. Repeat and put the second smallest value after the smallest value, etc
#With every iteration, we can confirm the front is the smallest values arranged, so there is no need to check them. 

def SelectionSort(list):
    n = len(list)
    #For each iteration, assume leftmost index value is lowest
    for i in range(n - 1):
        SmallestIndex = i
        #loop and check if any value is lower than leftmost index value
        for j in range(i + 1, n):
            if list[j] < list[SmallestIndex]:
                #If there is a lower value, let the index position j be position SmallestIndex 
                SmallestIndex = j
        #Swap the values of the index position SmallestIndex and index position i 
        list[i], list[SmallestIndex] = list[SmallestIndex], list[i]
    return list
#Time Complexity: O(n^2)
#As there are two nested loops
#Space Complexity: O(1)

SSList = [-10, 50, 20, 45, -20, -60, 5]
print(f"Selection Sort: {SelectionSort(SSList)}")

#Insertion Sort
#Take out the leftmost value first, assume it is in the right position. Proceed to take out the second leftmost value, compare with the first value, put it in front of the value is higher. Repeat.
#Every time a new value is taken out, insert it in its right position to sort it. So we are slowly inserting the values inside a sorted sequence. (Imagine sorting poker cards)

def InsertionSort(list):
    n = len(list)
    for i in range(1, n):
        #First assume first item is in proper position
        value = list[i]
        pos = i - 1
        #find the correct insertion point within the sorted sequence, while moving the whole list to the right each time to make space.
        while pos >= 0 and value < list[pos]:
            #move the values to the right by one position
            list[pos + 1] = list[pos]
            #decrease pos by one, remember that i is the counter to iterate, and pos is just i-1.
            pos = pos - 1
    #finally, we insert the value in its proper position inside the sorted sequence.
        list[pos+1] = value
    return list


#Time Complexity: O(n^2)
#for loop + while loop 
#Space Complexity: O(1)
ISList = [30, 50, 69, 75, 45, 69, 100]
print(f"Insertion Sort: {InsertionSort(ISList)}")

#Quick Sort
#Uses partitioning, and recursion to divide and conquer 
#This is when Pivot is at the START
def partition_pivotstart(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort_pivotstart(array, start, end):
    if start >= end:
        return

    p = partition_pivotstart(array, start, end)
    quick_sort_pivotstart(array, start, p-1)
    quick_sort_pivotstart(array, p+1, end)
    return array


plist = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]

print(f"Quick Sorted w pivot at Start: {quick_sort_pivotstart(plist, 0, len(plist)-1)}")

#This is when pivot is at the END
def partition_pivotend(array, start, end):
    pivot = array[end]
    low = start 
    high = end - 1

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1



        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[end], array[low] = array[low], array[end]

    return low

def quick_sort_pivotend(array, start, end):
    if start >= end:
        return

    p = partition_pivotend(array, start, end)
    #recursively run the left side
    quick_sort_pivotend(array, start, p-1)
    #recursively run the right side
    quick_sort_pivotend(array, p+1, end)
    return array

#Time Complexity: O(n) * O(log2 n) = O(nlog n) Average, O(n^2) worst case
#Consist of Breaking up the arrays + Partition (comparison and swap)
#We can keep breaking up the arrays to half each time, like binary search, thus O(log2 n)
#Each partition has n comparison and maximum n/2 swap (Even if we swap every value, it will only swap half of left with half of right), so O(n)
#In total, O(nlog n) average
#Space Complexity: O(log n)

plist2 = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
print(f"Quick Sorted w Pivot at End: {quick_sort_pivotend(plist2, 0, len(plist2)-1)}")

#Merge Sort 
#Take an array and keep splitting it into half and perform merge sort recursively until they are all single cell only.
#Once they are single cell, compare it with the other value before they are single cell, sort them accordingly.
#Once everything is sorted, merge it back into one array again.
def merge_sort(array):
    if len(array) > 1:

        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

unmerged_array = [12, 11, 13, 5, 6, 7]
merge_sort(unmerged_array)
merged_array = print(f"Merge sorted array: {unmerged_array}")






















#Heap Sort
