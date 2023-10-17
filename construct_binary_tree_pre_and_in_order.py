class TreeNode:
   def __init__(self, data, left = None, right = None):
      self.data = data
      self.left = left
      self.right = right
def print_tree(root):
   #print using inorder traversal
   if root is not None:
      print_tree(root.left)
      print(root.data, end = ' ')
      print_tree(root.right)
class Solution():
   def buildTree(self, preorder, inorder):
      if inorder:
         root = TreeNode(preorder.pop(0))
         root_index = inorder.index(root.data)
         root.left = self.buildTree(preorder,inorder[:root_index])
         root.right = self.buildTree(preorder,inorder[root_index+1:])
         return root
ob1 = Solution()
print_tree(ob1.buildTree([3,9,20,15,7], [9,3,15,20,7]))
