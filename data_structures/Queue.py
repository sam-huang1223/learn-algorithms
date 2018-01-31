class Queue:
    def __init__(self, queue=None):
        if not queue:
            self.queue = []
        else:
            self.queue = list(queue)

    def pop(self):
        return self.queue.pop(0)

    def push(self, element):
        self.queue.append(element)

    def get_size(self):
        return len(self.queue)