class Node:
    def __init__(self, val):
        self.left= None
        self.right = None
        self.val = val


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.__insert(self.root, val)

    def __insert(self, node: Node, val):
        if node.val == val:
            return
        elif val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self.__insert(node.left, val)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self.__insert(node.right, val)

    

    def level_order(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.val, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print() 


if __name__ == "__main__":
    bst = BinarySearchTree()
    for i in [8, 4, 12, 2, 6, 10, 16, 1, 5, 7, 100, 200, 150, 9, 15]:
        bst.insert(i)
    
    
    print("Level-Order Traversal:")
    bst.level_order()

