class Node():
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node
    def get_next(self):
        return self.next_node
    def set_next(self, next):
        self.next_node = next
    def get_data(self):
        return self.data
    def set_data(self, set_data):
        self.data = set_data

class LinkedList():
    def __init__(self, root = None): # none since it doesn't have anything in it yet
        self.root = root
        # size will initially be 0
        self.size = 0

    def get_size(self):
        return self.size

    def add (self, data):
        # creating new Node using the data
        new_node = Node(data, self.root)
        # setting root Nodes' pointer to the new Node
        self.root = new_node
        # increment size by 1
        self.size += 1

    def remove(self, data):
        # current node we are looking at, starting at the root
        current_node = self.root
        # need to change the pointer of the previous node
        prev_node = None
        # while there is still another Node, it's going to look at each Node
        while current_node:
            # if we find the node we are looking for
            if current_node.get_data() == data:
                # need to set the previous Node to point to the node AFTER the Node we are deleting
                if prev_node:
                    prev_node.set_next(current_node.get_next())
                # if there is no previous Node then we change the root to the next Node
                else:
                    self.root = current_node.get_next()
                # size decreases
                self.size -=1
                # returning if we have successfully removed the data
                return True
            # if we don't find the data in the current Node, we need to advance the pointers
            else:
                prev_node = current_node
                current_node = current_node.get_next()
        # if we were unable to find the data
        return False

    def find(self, data):
        # starting at the root Node
        current_node = self.root
        # while there is still another Node, it's going to look at each Node
        while current_node:
            # comparing the data of the Node with the data we are looking for
            if current_node.get_data() == data:
                # if the data is found, it'll be returned
                return data
            else:
                # if the data is not found, it will advance to the next Node
                current_node = current_node.get_next()
        # if it exits the loop without finding the data, it will return None
        return None

myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
myList.add(8)
print(myList.remove(17))
print(myList.find(4))



