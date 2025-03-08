
# Prompt: "Implement a Python function to search for a value in a binary search tree. Just show me the best way to do this and common practices and stuff. 
# The method should take the root of the tree and the value to be searched as parameters. 
# It should return True if the value is found in the tree, and False otherwise."

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search_bst(root, target):
    """Return True if target is found in the BST, else return False."""
    if root is None:
        return False
    if root.value == target:
        return True
    if target < root.value:
        return search_bst(root.left, target)
    else:
        return search_bst(root.right, target)

# Example usage (uncomment for testing):
# root = Node(10)
# root.left = Node(5)
# root.right = Node(15)
# print(search_bst(root, 5))   # Expected output: True
# print(search_bst(root, 12))  # Expected output: False
