# Rectangle.py



# Prompt: "I need to create a class called Rectangle that has attributes for length and width.
# How should I start defining this class in Python?"
# ChatGPT response: "Define a class with an __init__ method that initializes the length and width attributes."

class Rectangle:
    def __init__(self, length, width):
        # Prompt: "Should I assign the parameters to self.length and self.width?"
        # ChatGPT response: "Yes, use self.length and self.width to store the provided values."
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Prompt: "Now, I want to instantiate the Rectangle class with a length of 5 and a width of 3.
# How do I then print the area of the rectangle?"
# ChatGPT response: "Create an object of the class with the specified values and call the area method.
# Use the if __name__ == '__main__': block for proper execution."

if __name__ == '__main__':
    rect = Rectangle(5, 3)
    print("The area of the rectangle is:", rect.area())
