#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    pass

def greet(name):
    print  (f"Hello,{name}!")
    pass

def greet_with_default(name="programmer"):
    print(f"Hello,{name}!")
    pass

def add(num1, num2):
    sum = add(45 + 55)
    return sum 
    pass

def halve(number):
    return number /2
    pass

def greet_programmer():
    """
    Greets a programmer.
    Equivalent to the JavaScript function `greetProgrammer()`.
    """
    print("Hello, programmer!")

# /*
#   You should be able to call this function with one argument and see its output in the terminal:
#   greet("Naureen");
#   => "Hello, Naureen!"
# */
def greet(name):
    """
    Greets a person by their name.
    Uses an f-string, which is Python's equivalent to JavaScript's template literal.
    """
    print(f"Hello, {name}!")

# /*
#   You should be able to call this function with no arguments and see its output in the terminal:
#   greetWithDefault();
#   => "Hello, programmer!"
#
#   You should also be able to call this function with one argument and see its output in the terminal:
#   greetWithDefault("Sunny");
#   => "Hello, Sunny!"
# */
def greet_with_default(name="programmer"):
    """
    Greets a person, with a default name if none is provided.
    Python handles default parameters directly in the function definition.
    """
    print(f"Hello, {name}!")

# /*
#   You should be able to call this function with two arguments and get back its return value:
#   const sum = add(1, 2);
#   console.log(sum);
#   => 3
# */
def add(num1, num2):
    """
    Returns the sum of two numbers.
    """
    return num1 + num2

# /*
#   You should be able to call this function with one argument and get back its return value:
#   const result = halve(4);
#   console.log(result);
#   => 2
#
#   If the function is called with an argument that isn't a number, it should return null:
#   const result = halve("two")
#   => null
# */
def halve(number):
    """
    Halves a number. Returns None if the input is not a number.
    `isinstance(number, (int, float))` is the standard Python way to check for number types.
    `None` is the Python equivalent of JavaScript's `null`.
    """
    if not isinstance(number, (int, float)):
        return None
    
    return number / 2

# Example usage to demonstrate they work as expected
if __name__ == "__main__":
    print("\n--- Testing greet_programmer() ---")
    greet_programmer() # Hello, programmer!

    print("\n--- Testing greet() ---")
    greet("Naureen") # Hello, Naureen!

    print("\n--- Testing greet_with_default() ---")
    greet_with_default() # Hello, programmer!
    greet_with_default("Sunny") # Hello, Sunny!

    print("\n--- Testing add() ---")
    sum_result = add(1, 2)
    print(f"The sum of 1 and 2 is: {sum_result}") # 3

    print("\n--- Testing halve() ---")
    halve_result1 = halve(4)
    print(f"Half of 4 is: {halve_result1}") # 2.0
    
    halve_result2 = halve("two")
    print(f"Half of 'two' is: {halve_result2}") # None

