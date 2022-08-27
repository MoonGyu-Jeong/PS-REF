# -*- coding: utf-8 -*-
# Stack�� �� �� �������� �ڷḦ �ְų� �� �� �ִ� ���� ����(LIFO - Last In First Out)�� �����͸� �����ϴ� ������ ���Ѵ�.

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        pop_object = None
        if self.isEmpty():
            print("Stack is Empty")
        else:
            pop_object = self.stack.pop()
        
        return pop_object
    
    def top(self):
        top_obejct = None
        if self.isEmpty():
            print("Stack is Empty")
        else:
            top_object = self.stack[-1]
        return top_object
    
    def isEmpty(self):
        is_empty = False
        if len(self.stack) == 0:
            is_empty = True
        return is_empty

# ������� Stack�� ���� �� �ϳ��� ���� ȭ�鿡 ���
if __name__ == '__main__':
    test_case = [1,2,3,4,5]
    stk = Stack()
    for i in test_case:
        stk.push(i)
    
    for j in stk.stack:
        print(j)