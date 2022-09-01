# Importing 'heapq' to implemnet heap queue
import heapq
li = [5, 7, 9, 1, 3]

heapq.heapify(li)

print(f'The created heap is: {list(li)}')

heapq.heappush(li, 4)

print(f'The modified heap after push is: {list(li)}')

print(f'The popped and smallest element is: {heapq.heappop(li)}')
print('='*50)

li1 = [5, 1, 9, 4, 3]
li2 = [5, 7, 9, 4, 3]

heapq.heapify(li1)
heapq.heapify(li2)

print(f'The popped item using heappushpop() is: {heapq.heappushpop(li1, 2)}')

print(f'The popped item using heapreplace() is: {heapq.heapreplace(li2, 2)}')
print('='*50)

li3 = [6, 7, 9, 4, 3, 5, 8, 10, 1]

heapq.heapify(li3)

print(f'The 3 largest numbers in list are: {heapq.nlargest(3, li3)}')

print(f'The 3 smallest numbers in list are: {heapq.nsmallest(3, li3)}')
print('='*50)

heap = []
heapq.heapify(heap)

heapq.heappush(heap, -1*10)
heapq.heappush(heap, -1*30)
heapq.heappush(heap, -1*20)
heapq.heappush(heap, -1*400)

print(f'Head value of heap: {str(-1 * heap[0])}')

print("The heap elements: ")
for i in heap:
    print((-1*i), end=" ")
print('\n')

element = heapq.heappop(heap)

print("The heap elements: ")
for i in heap:
    print(-1*i, end=' ')