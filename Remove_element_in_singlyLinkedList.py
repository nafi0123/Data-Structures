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

def remove_element(head, val):
    dummy = SinglyLinkedListNode(0)
    dummy.next = head
    current = dummy
    
    while current.next is not None:
        if current.next.data == val:
            current.next = current.next.next
        else:
            current = current.next
    
    return dummy.next

def printLinkedList(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

if __name__ == '__main__':
    llist_count = int(input("Enter number of nodes: "))

    llist = SinglyLinkedList()

    print("Enter the nodes:")
    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    print("Original Linked List:")
    printLinkedList(llist.head)

    r_in = int(input("Enter the value to be removed: "))
    llist.head = remove_element(llist.head, r_in)

    print("Linked List after removal:")
    printLinkedList(llist.head)





