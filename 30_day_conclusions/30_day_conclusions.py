# Conclusions

# Now you're capable to begin to work with data analysis, data science, machine learning, or web development.

# So let's finish with a curiosity 

# One interesting thing that many people forget is that Python can introspect itself - that is, a program can inspect functions, code and objects at runtime.
# This is very "Pythonic" and widely usedd in frameworks(Django, FastAPI, pytest, etc). You can make a mini "function inspector" using the standard inspect module.

import inspect 

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def farewell(name: str):
    return f"Farewell, {name}! The code never ends... see you in the next project."

def inspect_function(func):
    print(f"\nFunction name: {func.__name__}")

    signature = inspect.signature(func)
    print(f"Parameters: {signature}")

    print(f"Docstring: {inspect.getdoc(func)}")

    print("\nSource code:")
    print(inspect.getsource(func))

inspect_function(calculate_average)
inspect_function(farewell)

print("-------------")

print(calculate_average([10,9,6,5,4,7,8]))
print(farewell("Francisco Rangel"))
