# Implementation by List
stack = []

stack.append('a')
stack.append('b')
stack.append('c')

print(stack) # ['a', 'b', 'c']

# LIFO(Last In First Out)
# pop() operations of list provides O(n) time complexity 
print(stack.pop()) # 'c'
print(stack.pop()) # 'b'
print(stack.pop()) # 'a'
print("="*40)

# Implementation by collections.deque
from collections import deque

stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')

print(stack) # ['a', 'b', 'c']

# LIFO
# pop() operations of deque provides O(1) time complexity
print(stack.pop()) # 'c'
print(stack.pop()) # 'b'
print(stack.pop()) # 'a'
print("="*40)

# Implementation by queue.LifoQueue
from queue import LifoQueue

stack = LifoQueue(3)

print(f"LifoQueue Size: {stack.qsize()}")

stack.put('a')
stack.put('b')
stack.put('c')

print(f"Full: {stack.full()}")
print(f"Size: {stack.qsize()}")

# LIFO
print(stack.get()) # 'c'
print(stack.get()) # 'b'
print(stack.get()) # 'a'

print(f"Empty: {stack.empty()}")
print("="*40)

# Implementation using a singly linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0
    
    # String representation of the stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]

    # Get the current size of stack
    def getSize(self):
        return self.size
    
    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0
    
    # Get the top item of the stack
    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        return self.head.next.value
    
    # Push a value into the stack
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
    
    # Remove a value from the stack and return
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

if __name__ == '__main__':
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f'Stack: {stack}')

    for _ in range(1, 6):
        remove = stack.pop()
        print(f'Pop: {remove}')
    print(f'Rest of Stack: {stack}')