from collections import deque

queue = deque(['name', 'age', 'DOB'])
print(queue)

# using append() to insert element at right end
queue.append(4)
print(queue)

# using appendleft() to insert element at left end
queue.appendleft(6)
print(queue)

# using pop() to delete element from right end
queue.pop()
print(queue)

# using popleft() to delete element from left end
queue.popleft()
print(queue)

# using index() to print the first occurrence of 'age'
print(queue.index('age',0,4))

# using insert() to insert the value 'MOON' at 5th position
queue.insert(2, 'MOON')
print(queue)

# using count() to count the occurrences of 'MOON'
print(queue.count('MOON'))

queue.remove('MOON')
print(queue)

# initializing deque
queue = deque([1,2,3])

# using extend() to add numbers to right end
queue.extend([4,5,6])
print(queue)

# using extendleft() to add numbers to left end
queue.extendleft([7,8,9])
print(queue)

# using rotate() to rotate the deque
queue.rotate(-3)
print(queue)

# using reverse() to reverse the deque
queue.reverse()
print(queue)