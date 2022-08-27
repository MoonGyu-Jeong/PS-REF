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

# Implementation by queue.LifoQueue

from queue import LifoQueue

stack = LifoQueue(3)

print(stack.qsize())

stack.put('a')
stack.put('b')
stack.put('c')

print("Full: ", stack.full())
print("Size: ", stack.qsize())

# LIFO
print(stack.get()) # 'c'
print(stack.get()) # 'b'
print(stack.get()) # 'a'

print("Empty: ", stack.empty())