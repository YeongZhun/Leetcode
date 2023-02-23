"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""
#Solution 1, the easiest, using python isalnum() and reverse list method, but might not be what interviewer want
class Solution1():
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                #return lower case, add on to string if c is alpha numerical (so space, commas, symbols, etc will be removed)
                newStr += c.lower()
        #newStr[::-1] reverses the string, and if string is palindrome, return statement would be True.
        return newStr == newStr[::-1]

#Time Complexity: O(n) , iterate through the array once
#Space Complexity, O(n) , we need to create a new array to store the reversed string.

#Solution 2, writing own function to check if character is alpha numerical using ASCII, and using two pointers on both ends of the string 
class Solution2():
    def isPalindrome2(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left < right:
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while right > left and not self.alphaNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    #function to check if char is alpha numerical using ASCII values
    def alphaNum(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))

test_solution2 = Solution2()
string1 = "A man, a plan, a canal: Panama"
string2 = "race a car"

print(f"string1 test: {test_solution2.isPalindrome2(string1)}")
print(f"string1 test: {test_solution2.isPalindrome2(string2)}")

#Time Complexity: O(n) , we need to iterate through the whole array once
#Space Complexity: O(1) , using 2 pointers, no creation of arrays