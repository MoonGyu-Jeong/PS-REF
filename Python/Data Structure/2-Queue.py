# Implementaion using list
queue = []

queue.append('a')
queue.append('b')
queue.append('c')

print(queue)

# pop() operations of list provides O(n) time complexity 
print(queue.pop(0)) # 'a'
print(queue.pop(0)) # 'b'
print(queue.pop(0)) # 'c'
print("="*40)

# Implementation using collections.deque
from collections import deque

q = deque()

q.append('a')
q.append('b')
q.append('c')

print(q)

# pop() operations of deque provides O(1) time complexity 
print(q.popleft()) # 'a'
print(q.popleft()) # 'b'
print(q.popleft()) # 'c'
print("="*40)

# Implementation using queue.Queue
from queue import Queue

q = Queue(maxsize=3)

print(q.qsize())

q.put('a')
q.put('b')
q.put('c')

print(f"Full: {q.full()}")

print(q.get()) # 'a'
print(q.get()) # 'b'
print(q.get()) # 'c'

q.put(1)
print(f"Empty: {q.empty()}")
print(f"Full: {q.full()}")