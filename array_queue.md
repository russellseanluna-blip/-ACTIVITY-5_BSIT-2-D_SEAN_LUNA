class CircularQueue:
    def __init__(self, capacity):
        self.items = [None] * capacity
        self.start = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == len(self.items)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue is full. Cannot add another item.")

        position = (self.start + self.count) % len(self.items)
        self.items[position] = value
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty. No item to remove.")

        removed_item = self.items[self.start]
        self.start = (self.start + 1) % len(self.items)
        self.count -= 1
        return removed_item

    def peek_front(self):
        if self.is_empty():
            raise IndexError("No items available in the queue.")

        return self.items[self.start]

    def display(self):
        result = []
        for i in range(self.count):
            position = (self.start + i) % len(self.items)
            result.append(self.items[position])

        print("Current Queue:", result)


if _name_ == "_main_":
    print("=== CIRCULAR QUEUE DEMONSTRATION ===")

    my_queue = CircularQueue(5)

    my_queue.enqueue(10)
    my_queue.enqueue(20)
    my_queue.enqueue(30)

    my_queue.display()
    print("First Item:", my_queue.peek_front())
    print("Removed Item:", my_queue.dequeue())

    my_queue.display()
