# Employee.py


# Prompt: "I need to create a class called Employee with attributes name and salary. How do I start?"
# ChatGPT response: "Define a class with an __init__ method that takes name and salary as parameters."
class Employee:
    def __init__(self, name, salary):
        # Prompt: "Should I store the parameters as instance attributes?"
        # ChatGPT response: "Yes, assign them to self.name and self.salary."
        self.name = name
        self.salary = salary

    def increase_salary(self, percentage):
        # Prompt: "How do I increase the salary by a given percentage?"
        # ChatGPT response: "Multiply the current salary by (1 + percentage/100) to increase it."
        self.salary *= (1 + percentage / 100)

# Prompt: "Now, instantiate an Employee object with name 'John' and salary 5000,
# increase his salary by 10%, and print the updated salary."
# ChatGPT response: "Create an Employee object, call the increase_salary method, and then print the updated salary."
if __name__ == '__main__':
    employee = Employee("John", 5000)
    employee.increase_salary(10)  # Increase salary by 10%
    print("Updated salary for", employee.name, "is:", employee.salary)
