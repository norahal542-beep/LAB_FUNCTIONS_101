# --- Part 1: Main Task ---
def print_pattern(n: int) -> None:
    """Prints a reverse counting number pattern from n down to 1."""
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

# 1. Print the documentation as required
print(print_pattern._doc_)

# 2. Call the function
print_pattern(5)

print("-" * 20)

# --- Bonus Task ---
def get_pattern_string(n: int) -> str:
    """Returns a reverse counting number pattern as a formatted string."""
    result = ""
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            result += f"{j} "
        result += "\n"
    return result

# Assign to variable and print
pattern_result = get_pattern_string(5)
print(pattern_result)