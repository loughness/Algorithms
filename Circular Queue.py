class circularQueue:
    # k sets the size of the queue
    def __init__(self, k):
        self.circular_queue = [None] * k
        self.head = 0
        self.tail = 0
        self.size = 0
        self.k = k

    def enQueue (self, item):
        if self.isFull():
            return False
        self.circular_queue[self.tail] = item
        self.size += 1
        self.tail = (self.tail + 1) % self.k

    def deQueue (self):
        if self.isEmpty():
            return False
        self.circular_queue[self.head] = None
        self.size -= 1
        self.head = (self.head + 1) % self.k
        return True

    def First (self):
        if self.isEmpty():
            return -1
        print (f'first element: {self.circular_queue[self.head]}')

    def Last (self):
        if self.isEmpty():
            return -1
        # we need the -1 as the self.tail keeps track of the position for the next value to be added
        print (f'last element: {self.circular_queue[self.tail - 1]}')

    def isFull (self):
        if self.size == self.k:
            return True
        return False

    def isEmpty (self):
        if self.size == 0:
            return True
        return False

    def show(self):
        print (self.circular_queue)

    def print_values(self):
        onlyValues = []
        for item in self.circular_queue:
            if item != None:
                onlyValues.append(item)

        print (onlyValues)

cq = circularQueue(7)
cq.show()
cq.enQueue(11)
cq.enQueue(2)
cq.enQueue(7)
cq.enQueue(22)
cq.enQueue(9)

cq.show()

cq.deQueue()

cq.show()

cq.print_values()