class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def reversePrint(llist):
    # Write your code here
    if llist is None:
        return llist
    reversePrint(llist.next)
    print(llist.data)
if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    reversePrint(llist.head)


# Time Complexity: O(N), Visiting over every node one time 
# Auxiliary Space: O(N), Function call stack space


"""============================================================""""""
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

class Solution:
    def reverseList(self, head):
        node=None
        while head:
            temp=head.next
            head.next=node
            node=head
            head=temp
        return node

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')
        node = node.next
        if node:
            print(sep, end='')

if __name__ == '__main__':
    llist_count = int(input("Enter the number of nodes in the list: "))

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input("Enter node value: "))
        llist.insert_node(llist_item)

    solution = Solution()
    reversed_head = solution.reverseList(llist.head)
    print_singly_linked_list(reversed_head, ' ')

# Time Complexity: O(N), Visiting over every node one time 
# Auxiliary Space: O(1)
    
