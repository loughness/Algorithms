class Queue:
    def __init__(self):
        self.queue = []

    def enqueue (self, item):
        self.queue.append(item)

    def dequeue (self):
        if len (self.queue) >= 1:
            # pop the 0th element
            return self.queue.pop(0)
        else:
            return None

    def show (self):
        print (self.queue)

q = Queue()

q.enqueue(10)
q.enqueue(7)
q.enqueue(11)
q.enqueue(2)
q.enqueue(99)

q.show()

print(f'dequeued element: {q.dequeue()}')

q.show()