class StackArray:
    def __init__(self, size):
        self.items = [None] * size
        self.top_index = -1

    def is_empty(self):
        return self.top_index == -1

    def is_full(self):
        return self.top_index == len(self.items) - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack is full. Cannot add more elements.")

        self.top_index += 1
        self.items[self.top_index] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty. Nothing to remove.")

        removed_item = self.items[self.top_index]
        self.top_index -= 1
        return removed_item

    def peek(self):
        if self.is_empty():
            raise IndexError("There are no elements in the stack.")

        return self.items[self.top_index]

    def display(self):
        print("Current Stack:", self.items[:self.top_index + 1])


if _name_ == "_main_":
    print("=== STACK ARRAY DEMONSTRATION ===")

    my_stack = StackArray(5)

    my_stack.push(15)
    my_stack.push(25)
    my_stack.push(35)

    my_stack.display()
    print("Top Element:", my_stack.peek())
    print("Removed Element:", my_stack.pop())

    my_stack.display()
