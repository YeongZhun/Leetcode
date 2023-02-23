"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
#Hint: Use hashmaps to classify each string alphabet and count the number of alphabets. Then compare t and s, their hashmaps should be identical.
class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        #if their string lengths are not equal, they are definitely not anagram.
        if len(s) != len(t):
            return False
        
        #Create empty hashmap for both t and s
        countS, countT = {}, {}

        #Doesn't matter len(s) or len(t), both are same length 
        for i in range(len(s)):
            #For each alphabet in the string, add them inside hashmap, increment by +1 if it appears again each time. dict.get method 2nd parameter is 0, so as to return 0 if key not found (which always happens the first time the alphabet is added)
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            #Same as above, use dict.get method so that key error wont occur if key dont exist.
            if countS[c] != countT.get(c, 0):
                return False
        #Since all the checks are completed, it is an anagram, return True.
        return True

#Time Complexity: O(n) or rather O(n+m), where n is string 1, m is string 2
#Space Complexity: O(n) or rather O(n+m), as we need to create hashmap for string 1 and string 2

"""
1) Possible to use Counter, a data structure in python for one line code. But probably not recommended in interview.
return Counter(s) == Counter(t)

2) Another possible improvement to space complexity is to use Sort() on both strings, and just compare them. But time complexity might suffer depending on the type of Sort used.
"""

test_solution = Solution()
s = "anagram"
t = "gramana"
print(test_solution.isAnagram(s, t))