import collections
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def rightSideView(root):
        res=[]
        q=collections.deque([root])
        while q:
            rightview=None
            ql=len(q)
            for i in range(ql):
                node=q.popleft()
                if node:
                    rightview=node
                    q.append(node.left)
                    q.append(node.right)
            if rightview:
                res.append(rightview.info)
        return res
tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))
for i in range(t):
    tree.create(arr[i])
print(rightSideView(tree.root))

