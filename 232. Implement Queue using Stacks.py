"""
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
"""
#Hint: Manipulate FIFO and LIFO, by just removing but readding the value.. 

class MyQueue(object):

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int):
        self.push_stack.append(x)
        
    def pop(self) -> int:
        #if self.empty() function is true, means both stacks are empty. Nothing to pop.
        if self.empty():
            return
        if len(self.pop_stack):
            #Small note, once something is "return", the function ends right here. 
            return self.pop_stack.pop()
        else:
            while len(self.push_stack):
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop()

    def peek(self) -> int:
        if self.empty():
            return
        if len(self.pop_stack):
            return self.pop_stack[-1]
        else:
            while len(self.push_stack):
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack[-1]
        

    def empty(self) -> bool:
        #Return True IF push_stack AND pop_stack is empty
        return len(self.push_stack)==False and len(self.pop_stack)==False

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
print("Pop: Expect to see 1")
param_2 = obj.pop()
print(param_2)

print("Peek: expect to see 2 (Because on top, we did obj.pop(), so value 1 should be gone already. Should show 2.")
param_3 = obj.peek()
print(param_3)

print("Empty: expect to return False if obj not empty")
param_4 = obj.empty()
print(param_4)