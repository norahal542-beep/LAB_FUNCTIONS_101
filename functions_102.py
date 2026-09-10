# 1. Global & Scope
global_var = "I am Global"

def check_scope():
    global global_var
    global_var = "Global Modified!"

# 2. Positional, Keyword Arguments & Default Values
def add_numbers(a: int, b: int = 10) -> int:
    """This function adds two numbers with a default value for b."""
    return a + b

# 3. Pass Keyword
def future_function():
    pass

# Testing
print(add_numbers(5))
print(add_numbers(a=3, b=7))
check_scope()
print(global_var)