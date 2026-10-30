class StackNode:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class StackLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_item = StackNode(data)
        new_item.next_node = self.head
        self.head = new_item

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot remove an item because the stack is empty.")

        removed_item = self.head.data
        self.head = self.head.next_node
        return removed_item

    def peek(self):
        if self.is_empty():
            raise IndexError("No items found in the stack.")

        return self.head.data

    def display(self):
        current_node = self.head
        stack_items = []

        while current_node is not None:
            stack_items.append(current_node.data)
            current_node = current_node.next_node

        print("Current Stack:", stack_items)


if _name_ == "_main_":
    print("=== LINKED LIST STACK DEMONSTRATION ===")

    my_stack = StackLinkedList()

    my_stack.push("Apple")
    my_stack.push("Banana")
    my_stack.push("Orange")

    my_stack.display()
    print("Top Item:", my_stack.peek())
    print("Removed Item:", my_stack.pop())

    my_stack.display()
