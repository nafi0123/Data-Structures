class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left=None 
        self.right=None

class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        
        q = [(root, str(root.val))]
        paths = []

        while q:
            node, path = q.pop(0)
            if not node.left or not node.right:
                paths.append(path)
            
            if node.left:
                q.append((node.left, path + "->" + str(node.left.val)))

            if node.right:
                q.append((node.right, path + "->" + str(node.right.val)))

        
        return paths



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

solution = Solution()
paths = solution.binaryTreePaths(root)
print("Final Paths:", paths)
