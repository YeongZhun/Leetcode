"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""
#Hint: Use a Stack

class Solution():
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")":"(", "]":"[", "}":"{"}

        for c in s:
            #check if each string is one of the closeToOpen keys
            if c in closeToOpen:
                #If yes, means this string is one of closing brackets ) ] }
                #First check if stack is EMPTY, as you cannot only have closing bracket when stack is empty
                #Second check if last string at the end of the stack (thus -1) is equals to the same matching value in the closeToOpen dict
                #e.g. if current c is closing bracket ")", stack[-1] is "(", closeToOpen[)] key will also return "(" value
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            #if c is NOT in closeToOpen dict, means it is an OPEN parenthesis/bracket for sure. This question assumes the string will only have brackets.
            #The rule is that you can have as many open brackets as you like, as long as you close them properly in correct order. Thus append the open bracket.
            else:
                stack.append(c)
        #Once all the string finish iterating, return True only if the stack is empty (because correct bracket pairs will get pop off the stack), otherwise false.
        return True if not stack else False

test_solution = Solution()
s = "((([])))"
print(test_solution.isValid(s))

#Time Complexity: O(n)
#We are going through the stack, every input character once only.
#Space Complexity: O(n)