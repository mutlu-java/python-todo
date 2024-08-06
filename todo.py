import os
import json

class TodoItem:
    def __init__(self, task):
        self.task = task
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{self.task} [{status}]"

class TodoList:
    def __init__(self, filename='todo_list.json'):
        self.filename = filename
        self.items = self.load_items()

    def add_item(self, task):
        self.items.append(TodoItem(task))
        self.save_items()

    def remove_item(self, index):
        if 0 <= index < len(self.items):
            del self.items[index]
            self.save_items()

    def mark_item_completed(self, index):
        if 0 <= index < len(self.items):
            self.items[index].mark_completed()
            self.save_items()

    def list_items(self):
        for index, item in enumerate(self.items):
            print(f"{index + 1}. {item}")

    def save_items(self):
        with open(self.filename, 'w') as file:
            json.dump([item.__dict__ for item in self.items], file)

    def load_items(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                items_data = json.load(file)
                return [TodoItem(**data) for data in items_data]
        return []

def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List:")
        todo_list.list_items()
        print("\nOptions:")
        print("1. Add a new task")
        print("2. Remove a task")
        print("3. Mark a task as completed")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_item(task)
        elif choice == '2':
            index = int(input("Enter the task number to remove: ")) - 1
            todo_list.remove_item(index)
        elif choice == '3':
            index = int(input("Enter the task number to mark as completed: ")) - 1
            todo_list.mark_item_completed(index)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
