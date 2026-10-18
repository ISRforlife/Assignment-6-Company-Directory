
# Company Directory Tree Assignment
# This program organizes employees using a binary tree.


class EmployeeNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    def __init__(self):
        self.root = None

    # Add an employee under a manager
    def insert(self, manager_name, employee_name, side, current_node=None):
        if self.root is None:
            print("Please add a team lead first.")
            return False

        side = side.strip().lower()
        manager_name = manager_name.strip()

        if side not in ("left", "right"):
            print("Please choose left or right.")
            return False

        if current_node is None:
            current_node = self.root

        # Search for the manager
        manager = self.find_manager(current_node, manager_name)

        if manager is None:
            print("Manager was not found.")
            return False

        # Check if the selected side is available
        if side == "left":
            if manager.left is not None:
                print("The left side is already taken.")
                return False

            manager.left = EmployeeNode(employee_name)

        else:
            if manager.right is not None:
                print("The right side is already taken.")
                return False

            manager.right = EmployeeNode(employee_name)

        print(f"{employee_name} added to the {side.upper()} of {manager_name}")
        return True

    # Recursively search the tree for a manager
    def find_manager(self, node, manager_name):
        if node is None:
            return None

        if node.name == manager_name:
            return node

        # Search the left branch
        found = self.find_manager(node.left, manager_name)

        if found is not None:
            return found

        # Search the right branch
        return self.find_manager(node.right, manager_name)

    # Recursively print the team structure
    def print_tree(self, node=None, level=0):
        if node is None:
            if level == 0:
                node = self.root
            else:
                return

        if node is None:
            print("The directory is empty.")
            return

        print("  " * level + "- " + node.name)

        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)


# Command line menu
def company_directory():
    tree = TeamTree()

    while True:
        print("\nTeam Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            if tree.root is not None:
                print("A team lead already exists.")
            else:
                name = input("Enter team lead's name: ").strip()

                if name:
                    tree.root = EmployeeNode(name)
                    print(f"{name} added as the team lead.")
                else:
                    print("Please enter a name.")

        elif choice == "2":
            manager = input("Enter the manager's name: ").strip()
            employee = input("Enter the new employee's name: ").strip()
            side = input(
                "Should this employee be on the LEFT or RIGHT? "
            ).strip().lower()

            if not employee:
                print("Please enter an employee name.")
            else:
                tree.insert(manager, employee, side)

        elif choice == "3":
            print("\nCurrent Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    company_directory()
