class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            nodes = [self.root]

            while True:
                check_node = nodes.pop(0)
                if check_node.left is None:
                    check_node.left = TreeNode(val)
                    return
                elif check_node.right is None:
                    check_node.right = TreeNode(val)
                    return
                else:
                    nodes.append(check_node.left)
                    nodes.append(check_node.right)


def check_binary_search_tree_(root, list=[]):
    if root.left:
        check_binary_search_tree_(root.left, list)

    list.append(root.val)

    if root.right:
        check_binary_search_tree_(root.right, list)

    if list != sorted(list) or len(list) > len(set(list)):
        return False
    else:
        return True

my_tree = BinaryTree()
for i in [1,2,3]:
    my_tree.insert(i)
print(check_binary_search_tree_(my_tree.root))
