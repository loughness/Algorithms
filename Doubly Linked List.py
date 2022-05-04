class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            current = self.head
            while current.next:
                current = current.next
            # set the previous node of the new node to the last node
            new_node.prev = current
            # set the next of the previous node to the one we want to append
            current.next = new_node
            new_node.next = None

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.prev = None
            new_node.next = self.head
            self.head = new_node

    def length(self):
        counter = 0
        current = self.head
        while current:
            counter += 1
            current = current.next
        return counter


    def insert_at(self, index, data):
        # validate
        if index >= self.length() or index < 0:
            print('Invalid index!')
        # if the index is zero, use the prepend function
        elif index == 0:
            self.prepend(data)
        # if the index equals to the length of the list,
        # meaning that we want to append to the end,
        # use the append function
        elif index == self.length():
            self.append(data)
        else:
            new_node = Node(data)
            current = self.head
            # get the node which is at our desired index - 1
            for _ in range (index - 1):
                # check if there is such a node
                if current:
                    current = current.next

            # set the next of the new node for the next of the node at position index - 1
            # new node's next is the node that we replace
            new_node.next = current.next
            # new node's previous node is at index - 1 ofc
            new_node.prev = current
            # index - 1's next is the new node
            current.next = new_node
            # if new_node.next:
            #     new_node.next.prev = new_node

    def show(self):
        current = self.head
        list = []
        while current:
            list.append(str (current.data))
            current = current.next
        print (' -> '.join (list))

dll = DoublyLinkedList()

dll.append(5)
dll.append(10)
dll.append(23)
dll.append(4)

dll.show()

dll.prepend(7)
dll.prepend(11)

dll.show()

print (f'The length of the list is: {dll.length()}')

dll.insert_at(5, 22)
dll.show()

print (f'The length of the list is: {dll.length()}')