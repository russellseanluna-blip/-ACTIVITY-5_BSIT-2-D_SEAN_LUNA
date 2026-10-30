class Element:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class QueueLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first is None

    def enqueue(self, data):
        new_element = Element(data)

        if self.is_empty():
            self.first = new_element
        else:
            self.last.next_node = new_element

        self.last = new_element

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty. No element to remove.")

        removed_data = self.first.data
        self.first = self.first.next_node

        if self.first is None:
            self.last = None

        return removed_data

    def peek_front(self):
        if self.is_empty():
            raise IndexError("The queue has no elements.")

        return self.first.data

    def display(self):
        current_node = self.first
        queue_items = []

        while current_node is not None:
            queue_items.append(current_node.data)
            current_node = current_node.next_node

        print("Current Queue:", queue_items)


if _name_ == "_main_":
    print("=== LINKED LIST QUEUE DEMONSTRATION ===")

    my_queue = QueueLinkedList()

    my_queue.enqueue("Task A")
    my_queue.enqueue("Task B")
    my_queue.enqueue("Task C")

    my_queue.display()
    print("First Element:", my_queue.peek_front())
    print("Removed Element:", my_queue.dequeue())

    my_queue.display()
