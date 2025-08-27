class QueueUsingTwoStacks:
    def __init__(self):
        self.stack_in = []   # For enqueue
        self.stack_out = []  # For dequeue

    def enqueue(self, item):
        self.stack_in.append(item)

    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            raise IndexError("Queue is empty")
        return self.stack_out.pop()

    def peek(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            raise IndexError("Queue is empty")
        return self.stack_out[-1]

    def is_empty(self):
        return not self.stack_in and not self.stack_out

    def size(self):
        return len(self.stack_in) + len(self.stack_out)


if __name__ == "__main__":

    # Example usage:
    q = QueueUsingTwoStacks()
    print(q.is_empty()) # False
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.dequeue())  # 1
    q.enqueue(4)
    # print(q.peek())     # 2
    print(q.dequeue())  # 2
    print(q.dequeue())  # 2
    print(q.dequeue())  # 2
    # print(q.is_empty()) # False
