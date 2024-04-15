class StringStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def push(self, item):
        """Put a string onto the stack if there is space."""
        if not self.is_full():
            self.stack.append(item)
            print(f"Pushed '{item}' onto the stack.")
        else:
            print("Failed to push: Stack is full.")

    def pop(self):
        """Remove and return the top string from the stack."""
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Failed to pop: Stack is empty.")
            return None

    def peek(self):
        """Return the top string without removing it from the stack."""
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty.")
            return None

    def is_full(self):
        """Check if the stack is full."""
        return len(self.stack) == self.capacity

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of strings in the stack."""
        return len(self.stack)

    def clear(self):
        """Clear all items from the stack."""
        self.stack = []
        print("Stack has been cleared.")

def display_menu():
    menu = """
1. Push a string to the stack
2. Pop a string from the stack
3. Check the number of strings in the stack
4. Check if the stack is empty
5. Check if the stack is full
6. Peek at the top string
7. Clear the stack
8. Exit
"""
    stack = StringStack(5)  # Fixed size of 5
    while True:
        print(menu)
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            item = input("Enter a string to push: ")
            stack.push(item)
        elif choice == '2':
            popped_item = stack.pop()
            if popped_item:
                print(f"Popped '{popped_item}' from the stack.")
        elif choice == '3':
            print(f"There are {stack.size()} strings in the stack.")
        elif choice == '4':
            print("Stack is empty." if stack.is_empty() else "Stack is not empty.")
        elif choice == '5':
            print("Stack is full." if stack.is_full() else "Stack is not full.")
        elif choice == '6':
            top_item = stack.peek()
            if top_item:
                print(f"The top string on the stack is '{top_item}'.")
        elif choice == '7':
            stack.clear()
        elif choice == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    display_menu()
