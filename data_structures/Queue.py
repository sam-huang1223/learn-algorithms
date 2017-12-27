class Queue:
    def __init__(self, queue=None):
        if not queue:
            self.queue = []
        else:
            self.queue = list(queue)

    def dequeue(self):
        return self.queue.pop(0)

    def enqueue(self, element):
        self.queue.append(element)