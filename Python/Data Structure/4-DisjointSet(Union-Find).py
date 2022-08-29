# Implementation using list
class DisjointSet:
    def __init__(self, n):
        self.data = list(range(n))
        self.size = n

    def find(self, index):
        return self.data[index]
    
    def union(self, x, y):
        x, y = self.find(x), self.find(y)

        if x == y:
            return
        
        for i in range(self.size):
            if self.find(i) == y:
                self.data[i] = x
    
    @property
    def length(self):
        return len(set(self.data))

# Implemntation using Tree
# union-by-size
class Unionbysize:
    def __init__(self, n):
        self.data = [-1 for _ in range(n)]
        self.size = n
    
    def find(self, index):
        value = self.data[index]
        if value < 0:
            return index
        return self.find(value)

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        
        if self.data[x] < self.data[y]:
            self.data[x] += self.data[y]
            self.data[y] = x
        else:
            self.data[y] += self.data[x]
            self.data[x] = y
        
        self.size -= 1

# union-by-height
class Unionbyheight:
    def __init__(self, n):
        self.data = [-1] * n
        self.size = n
    
    def find(self, index):
        value = self.data[index]
        if value < 0:
            return index
        
        return self.find(value)
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        
        if self.data[x] < self.data[y]:
            self.data[y] = x
        elif self.data[x] > self.data[y]:
            self.data[x] = y
        else:
            self.data[x] -= 1
            self.data[y] = x
        
        self.size -= 1

# path comprehension
class PathComprehension:
    def __init__(self, n):
        self.data = [-1 for _ in range(n)]
        self.size = n
    
    def upward(self, change_list, index):
        value = self.data[index]
        if value < 0:
            return index
        
        change_list.append(index)
        return self.upward(change_list, value)

    def find(self, index):
        change_list = []
        result = self.upward(change_list, index)

        for i in change_list:
            self.data[i] = result
        
        return result

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.data[x] < self.data[y]:
            self.data[y] = x
        elif self.data[x] > self.data[y]:
            self.data[x] = y
        else:
            self.data[x] -= 1
            self.data[y] = x
        
        self.size -= 1

if __name__ == '__main__':
    disjoint = DisjointSet(10)

    disjoint.union(0, 1)
    disjoint.union(1, 2)
    disjoint.union(2, 3)
    disjoint.union(4, 5)
    disjoint.union(5, 6)
    disjoint.union(6, 7)
    disjoint.union(8, 9)

    print(disjoint.data)
    print(disjoint.length)
    print('='*40)

    disjointtree = Unionbysize(10)

    disjointtree.union(0, 1)
    disjointtree.union(1, 2)
    disjointtree.union(2, 3)
    disjointtree.union(4, 5)
    disjointtree.union(5, 6)
    disjointtree.union(6, 7)
    disjointtree.union(8, 9)

    print(disjointtree.data)
    print(disjointtree.size)
    print('='*40)

    ubh = Unionbyheight(10)

    ubh.union(0, 1)
    ubh.union(1, 2)
    ubh.union(2, 3)
    ubh.union(4, 5)
    ubh.union(5, 6)
    ubh.union(6, 7)
    ubh.union(8, 9)

    print(ubh.data)
    print(ubh.size)
    print('='*40)

    pathComp = PathComprehension(10)

    pathComp.union(0, 1)
    pathComp.union(1, 2)
    pathComp.union(2, 3)
    pathComp.union(4, 5)
    pathComp.union(5, 6)
    pathComp.union(6, 7)
    pathComp.union(8, 9)

    print(pathComp.data)
    print(pathComp.size)