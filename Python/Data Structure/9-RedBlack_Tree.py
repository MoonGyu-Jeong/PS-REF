# https://lsh424.tistory.com/73

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = self.left = self.right = None
        self.color = 'Red' # Inserted Node is always Red

class RedBlackTree:

    def __init__(self):
        self.root = None
        self.inserted_node = None

    def insert(self, data, parent_node):
        self.root = self.insert_value(self.root, data, parent_node)
        self.insert_root(self.inserted_node)
        return 

    def insert_value(self, node, data, parent_node):
        if node is None:
            node = Node(data)
            node.parent = parent_node
            self.inserted_node = node
        else:
            if data <= node.data:
                node.left = self.insert_value(node.left, data, node)
            else:
                node.right = self.insert_value(node.right, data, node)
        return node

    def find(self, search_key):
        return self.find_value(self.root, search_key)
    
    def find_value(self, root, search_key):
        if root is None or root.data == search_key:
            return root
        elif search_key > root.data:
            return self.find_value(root.right, search_key)
        else:
            return self.find_value(root.left, search_key)

    # Finding grandparent node
    def find_grandparent_node(self, node):
        if node != Node and node.parent != Node:
            return node.parent.parent
        else:
            return None
    
    # Finding uncle node
    def find_uncle_node(self, node):
        grandparent_node = self.find_grandparent_node(node)
        if grandparent_node == None:
            return None
        
        if node.parent == grandparent_node.left:
            return grandparent_node.right
        else:
            return grandparent_node.left
    
    # case1. Root Node is always Black.
    def insert_root(self, node):
        if node.parent == None:
            node.color = 'Black'
        else:
            self.insert_case2(node)
    
    # case2. If parent node is Black, no neeed to perform. But Red, perform case3
    def insert_case2(self, node):
        if node.parent.color == 'Black':
            return
        else:
            self.insert_case3(node)
    
    # case3. If parent node and uncle node are Red, perform changing color. If not, perform case4
    def insert_case3(self, node):
        uncle = self.find_uncle_node(node)

        if uncle != None and uncle.color == 'Red':
            node.parent.color = 'Black'
            uncle.color = 'Black'
            grandparent = self.find_grandparent_node(node)
            grandparent.color = 'Red'
            self.insert_root(grandparent)
        else:
            self.insert_case4(node)
        
    # case4. Perform rotation
    def insert_case4(self, node):
        grandparent = self.find_grandparent_node(node)
        
        if node == node.parent.right and node.parent == grandparent.left:
            self.rotate_left(node.parent)
            node = node.left
        elif node == node.parent.left and node.parent == grandparent.right:
            self.rotate_right(node.parent)
            node = node.right
        self.insert_case5(node)
    
    # case5. Perform rotation
    def insert_case5(self, node):
        grandparent = self.find_grandparent_node(node)

        node.parent.color = 'Black'
        grandparent.color = 'Red'

        if node == node.parent.left:
            self.rotate_right(grandparent)
        else:
            self.rotate_left(grandparent)
    
    def rotate_left(self, node):
        c = node.right
        p = node.parent

        if c.left != None:
            c.left.parent = node
        
        node.right = c.left
        node.parent = c
        c.left = node
        c.parent = p

        if c.parent == None:
            self.root = c
        
        if p != None:
            if p.left == node:
                p.left = c
            else:
                p.right = c
    
    def rotate_right(self, node):
        c = node.left
        p = node.parent

        if c.right != None:
            c.right.parent = node
        
        node.left = c.right
        node.parent = c
        c.right = node
        c.parent = p

        if c.parent == None:
            self.root = c
        
        if p != None:
            if p.right == node:
                p.right = c
            else:
                p.left = c
    
def check(node):
    if not node.left == None: check(node.left)
    if node.parent != None:
        print(f'key: {node.data} parents: {node.parent.data} color: {node.color}')
    else:
        print(f'key: {node.data} parents: {node.parent} color: {node.color}')
    if not node.right == None: check(node.right)

def main():
    rbt = RedBlackTree()
    a = [2, 1, 8, 9, 7, 3, 6, 4, 5]
    for x in a:
        rbt.insert(x, None)
    check(rbt.root)

if __name__ == '__main__':
    main()