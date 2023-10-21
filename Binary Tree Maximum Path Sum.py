class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
class Solution:
    def maxPathSum(self, root):
        def solve(root,res):
            if root is None:
                return 0
            ls=solve(root.left,res)
            rs=solve(root.right,res)
            temp=max(max(ls,rs)+root.data,root.data)
            ans=max(temp,ls+rs+root.data)
            res[0]=max(res[0],ans)
            return temp
        res= [-100000]
        solve(root,res)
        return res[0]

ob = Solution()

tree = BinarySearchTree()


arr = [1,2,3]


for i in range(len(arr)):
    tree.create(arr[i])
print(ob.maxPathSum(tree.root))
