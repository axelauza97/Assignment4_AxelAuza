import sys


# GitHub is a platform for version control and collaboration, allowing multiple people to work on projects simultaneously.
# Branching in GitHub lets you create separate lines of development within a repository, enabling you to work on features or fixes independently
# before merging them back into the main codebase.
def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


try:
    # Get values from form data
    inputs = sys.argv[1:6]

    if len(inputs) < 5:
        print("<html><body><p>Error: Five input values are required.</p></body></html>")
        raise "Error"

    # Check if all inputs are numeric
    if not all(is_numeric(val) for val in inputs):
        print("<html><body><p>Error: All inputs must be numeric.</p></body></html>")
        raise "Error"

    # Convert inputs to floats
    numbers = [float(val) for val in inputs]

    # Generate HTML output
    print("<html><head><title>Calculation Results</title></head><body>")
    print(f"<h2>Inputs: {', '.join(f'{val}' for val in numbers)}</h2>")

    # Check for negative values
    if any(num < 0 for num in numbers):
        print("<p>Warning: One or more values are negative.</p>")

    # Calculate the average
    average = sum(numbers) / len(numbers)
    print(f"<p>Average: {average}</p>")
    if average > 50:
        print("<p>The average is greater than 50.</p>")
    else:
        print("<p>The average is 50 or less.</p>")

    # Bitwise operation to check if the count of positive numbers is even or odd
    positive_count = sum(1 for num in numbers if num > 0)
    if positive_count & 1:
        print("<p>The count of positive numbers is odd.</p>")
    else:
        print("<p>The count of positive numbers is even.</p>")

    # Create a list of values greater than 10 and sort it
    greater_than_ten = [num for num in numbers if num > 10]
    sorted_greater_than_ten = sorted(greater_than_ten)
    print("<p>Original List: ", numbers, "</p>")
    print("<p>Values Greater Than 10 (Sorted): ", sorted_greater_than_ten, "</p>")

    print("</body></html>")


except (ValueError, TypeError) as e:
    print(
        "<html><body><p>Error: Invalid input. Please enter numeric values for a, b, and c.</p></body></html>"
    )
