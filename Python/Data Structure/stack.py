# -*- coding: utf-8 -*-
# Stack은 한 쪽 끝에서만 자료를 넣거나 뺄 수 있는 선형 구조(LIFO - Last In First Out)로 데이터를 저장하는 형식을 말한다.

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

# 순서대로 Stack에 넣은 후 하나씩 꺼내 화면에 출력
if __name__ == '__main__':
    test_case = [1,2,3,4,5]
    stk = Stack()
    for i in test_case:
        stk.push(i)
    
    for j in stk.stack:
        print(j)