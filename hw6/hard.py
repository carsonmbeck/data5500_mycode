"""
ChatGPT Prompt:
"I need to develop an efficient algorithm in Python that finds the maximum difference between any two numbers in a list. 
I’d like to achieve this in a single pass through the data, ensuring O(n) time complexity. How can I implement such a solution?"
"""

def max_difference(arr):
    """
    Returns the maximum difference between any two numbers in the array.
    
    Time Complexity: O(n)
    Explanation: The function scans the list once to determine both the minimum and maximum values, 
    and then computes their difference.
    """
    if len(arr) < 2:
        return 0  # No meaningful difference if fewer than 2 elements.
    
    min_val = max_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    return max_val - min_val

if __name__ == "__main__":
    test_array = [10, 3, 5, 6, 20]
    print("Array:", test_array)
    print("Maximum difference:", max_difference(test_array))
