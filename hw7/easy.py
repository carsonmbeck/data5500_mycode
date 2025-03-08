
# Prompt: "Write a Python function to insert a value into a binary search tree. 
# The function should take the root of the tree and the value to be inserted as parameters."

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_into_bst(root, value):

    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert_into_bst(root.left, value)
    else:
        root.right = insert_into_bst(root.right, value)
    return root

# Example usage (uncomment for testing):
root = None
for val in [10, 5, 15, 3, 7, 12, 18]:
    root = insert_into_bst(root, val)
