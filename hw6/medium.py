"""
ChatGPT Prompt:
"I'm trying to analyze an array of integers and need to identifyy the second largest element. 
What would be a clear and efficient approach that minimizes the number of passes over the data? 
Please include the Big O analysis of your method again that would be helpful. Thanks."
"""

def second_largest(arr):
    """
    Returns the second largest number in the array.
    
    Time Complexity: O(n)
    Explanation: We traverse the list only once while keeping track of the largest and second largest numbers.
    """
    if len(arr) < 2:
        return None  # Not enough elements for a second largest number.
    
    # Initialize largest and second with very small values to support negative numbers.
    largest = second = float('-inf')
    
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num
    
    return second if second != float('-inf') else None

if __name__ == "__main__":
    test_array = [12, 35, 1, 10, 34, 1]
    print("Array:", test_array)
    print("Second largest:", second_largest(test_array))
