from array_stack import StackArray
from linked_stack import StackLinkedList
from array_queue import CircularQueue
from linked_queue import QueueLinkedList


def check_parentheses(expression):
    stack = StackLinkedList()
    brackets = {')': '(', ']': '[', '}': '{'}

    for symbol in expression:
        if symbol in brackets.values():
            stack.push(symbol)
        elif symbol in brackets:
            if stack.is_empty() or stack.pop() != brackets[symbol]:
                return False

    return stack.is_empty()


class PrintingTask:
    def __init__(self, filename, page_count):
        self.filename = filename
        self.page_count = page_count

    def __str__(self):
        return f"{self.filename} - {self.page_count} pages"


class PrinterSimulation:
    def __init__(self):
        self.task_queue = QueueLinkedList()

    def add_printing_task(self, filename, page_count):
        task = PrintingTask(filename, page_count)
        self.task_queue.enqueue(task)
        print(f"New task added: {task}")

    def print_next_task(self):
        if self.task_queue.is_empty():
            print("The printing queue is currently empty.")
            return

        task = self.task_queue.dequeue()
        print(f"Currently printing: {task} - Completed!")

    def display_tasks(self):
        print("--- Current Printing Tasks ---")
        current_node = self.task_queue.first
        number = 1

        while current_node:
            print(f"{number}. {current_node.data}")
            current_node = current_node.next_node
            number += 1

        print("------------------------------")


def main():
    while True:
        print("\n===== STACK AND QUEUE OPERATIONS =====")
        print("[1] Array Stack Demonstration")
        print("[2] Linked Stack Demonstration")
        print("[3] Array Queue Demonstration")
        print("[4] Linked Queue Demonstration")
        print("[5] Check Balanced Parentheses")
        print("[6] Printer Queue Demonstration")
        print("[0] Quit Program")

        option = input("Select an option: ")

        if option == "1":
            print("\n--- ARRAY STACK ---")
            capacity = int(input("Set stack size: "))
            stack = StackArray(capacity)

            while True:
                command = input("(p)ush, (po)p, (pe)ek, (d)isplay, (b)ack: ").lower()

                if command == "p":
                    item = input("Enter an item: ")
                    try:
                        stack.push(item)
                    except Exception as error:
                        print(error)

                elif command == "po":
                    try:
                        print("Removed item:", stack.pop())
                    except Exception as error:
                        print(error)

                elif command == "pe":
                    try:
                        print("Top item:", stack.peek())
                    except Exception as error:
                        print(error)

                elif command == "d":
                    stack.display()

                elif command == "b":
                    break

        elif option == "2":
            print("\n--- LINKED STACK ---")
            stack = StackLinkedList()

            while True:
                command = input("(p)ush, (po)p, (pe)ek, (d)isplay, (b)ack: ").lower()

                if command == "p":
                    item = input("Enter an item: ")
                    stack.push(item)

                elif command == "po":
                    try:
                        print("Removed item:", stack.pop())
                    except Exception as error:
                        print(error)

                elif command == "pe":
                    try:
                        print("Top item:", stack.peek())
                    except Exception as error:
                        print(error)

                elif command == "d":
                    stack.display()

                elif command == "b":
                    break

        elif option == "3":
            print("\n--- ARRAY QUEUE ---")
            capacity = int(input("Set queue size: "))
            queue = CircularQueue(capacity)

            while True:
                command = input("(e)nqueue, (d)equeue, (pe)ek, (di)splay, (b)ack: ").lower()

                if command == "e":
                    item = input("Enter an item: ")
                    try:
                        queue.enqueue(item)
                    except Exception as error:
                        print(error)

                elif command == "d":
                    try:
                        print("Removed item:", queue.dequeue())
                    except Exception as error:
                        print(error)

                elif command == "pe":
                    try:
                        print("Front item:", queue.peek_front())
                    except Exception as error:
                        print(error)

                elif command == "di":
                    queue.display()

                elif command == "b":
                    break

        elif option == "4":
            print("\n--- LINKED QUEUE ---")
            queue = QueueLinkedList()

            while True:
                command = input("(e)nqueue, (d)equeue, (pe)ek, (di)splay, (b)ack: ").lower()

                if command == "e":
                    item = input("Enter an item: ")
                    queue.enqueue(item)

                elif command == "d":
                    try:
                        print("Removed item:", queue.dequeue())
                    except Exception as error:
                        print(error)

                elif command == "pe":
                    try:
                        print("Front item:", queue.peek_front())
                    except Exception as error:
                        print(error)

                elif command == "di":
                    queue.display()

                elif command == "b":
                    break

        elif option == "5":
            print("\n--- BALANCED PARENTHESES CHECKER ---")
            expression = input("Type an expression: ")

            if check_parentheses(expression):
                print("The parentheses are properly balanced.")
            else:
                print("The parentheses are not balanced.")

        elif option == "6":
            print("\n--- PRINTER QUEUE ---")
            printer = PrinterSimulation()

            while True:
                command = input("(a)dd task, (p)rint next, (s)how tasks, (b)ack: ").lower()

                if command == "a":
                    filename = input("Enter file name: ")
                    page_count = int(input("Enter total pages: "))
                    printer.add_printing_task(filename, page_count)

                elif command == "p":
                    printer.print_next_task()

                elif command == "s":
                    printer.display_tasks()

                elif command == "b":
                    break

        elif option == "0":
            print("Program terminated. Thank you!")
            break


if _name_ == "_main_":
    main()
