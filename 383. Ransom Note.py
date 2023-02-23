"""Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote."""
#Hint: Many ways to do this. Can use counter data structure, hashmaps, and also one last method that replaces magazine string to empty and check the condition

#Solution 1: Counter
from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)

        for key in ransom_counter:
            if ransom_counter[key] > magazine_counter[key]:
                return False
        return True

#Solution 2: Hashmaps
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_dict = {}
        magazine_dict = {}

        for i in ransom_dict:
            if i not in ransom_dict:
                ransom_dict[i] = 1
            else:
                ransom_dict[i] += 1
        
        for i in magazine_dict:
            if i not in magazine_dict:
                magazine_dict[i] = 1
            else: 
                magazine_dict[i] += 1

        for i in ransom_dict:
            if i not in magazine_dict:
                return False
            elif ransom_dict[i] > magazine_dict[i]:
                return False
        return True

#Solution 3: For loop to check and replace magazine strings to empty
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i,"",1)
            else:
                return False
        return True

