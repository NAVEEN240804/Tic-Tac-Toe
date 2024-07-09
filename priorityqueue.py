import queue

class PriorityQueue:
    def __init__(self):
        self.priority_queue = queue.PriorityQueue()

    def is_empty(self):
        return self.priority_queue.empty()

    def enqueue(self, item, priority):
        self.priority_queue.put((priority, item))

    def dequeue(self):
        if not self.is_empty():
            return self.priority_queue.get()[1]
        else:
            raise IndexError("dequeue from empty priority queue")

    def peek(self):
        if not self.is_empty():
            return self.priority_queue.queue[0][1]
        else:
            raise IndexError("peek from empty priority queue")

    def size(self):
        return self.priority_queue.qsize()
