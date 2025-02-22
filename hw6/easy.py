"""
ChatGPT Prompt:
"I'm working on a basic data processing task in Python. What's an efficient way to calculate the sum of all numbers in a list? 
Also, could you explain the time complexity of your approach using Big O notation?"
"""

def array_sum(arr):
    """
    Returns the sum of all elements in the array.
    
    Time Complexity: O(n)
    Explanation: The function iterates through each element of the list exactly once, accumulating the total.
    """
    total = 0
    for num in arr:
        total += num
    return total

if __name__ == "__main__":
    test_array = [1, 2, 3, 4, 5]
    print("Array:", test_array)
    print("Sum:", array_sum(test_array))
