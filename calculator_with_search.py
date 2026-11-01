def basic_calculate(first_number, operator, second_number):
    """Calculate two numbers with a basic arithmetic operator.

    Returns the numeric result for a supported operation, or None when
    attempting to divide by zero. Raises ValueError for unsupported operators.
    """
    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        if second_number == 0:
            return None
        result = first_number / second_number
    else:
        raise ValueError(f"Unsupported operator: {operator}")

    # return sends the result back to the caller instead of printing it.
    return result


def equation_solver_menu():
    """Prompt for and solve an equation in the form a*x + b = target.

    Reports invalid input and equations with no unique solution. For an
    equation with a nonzero coefficient, prints the approximate x value
    returned by solve_for_x().
    """
    print("Solve an equation in the form a*x + b = target.")

    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter constant b: "))
        target = float(input("Enter target value: "))
    except ValueError:
        print("Please enter valid numbers for a, b, and the target.")
        return

    if a == 0:
        if b == target:
            print("Every value of x is a solution.")
        else:
            print("There is no solution.")
        return

    best_x = solve_for_x(a, b, target)
    print(f"The approximate solution is x = {best_x}.")


def solve_for_x(a, b, target):
    """Find the x value from -100.0 to 100.0 that best fits a*x + b = target.

    Tests 2,001 candidates in increments of 0.1 and returns the candidate
    whose predicted result is closest to the target.
    """
    best_x = -100.0
    smallest_difference = float("inf")

    for index in range(2001):
        x = -100.0 + index * 0.1
        predicted_result = a * x + b
        difference = abs(predicted_result - target)

        # Keep the candidate that most closely matches the target.
        if difference < smallest_difference:
            smallest_difference = difference
            best_x = x

    return best_x


def visualize_search(a, b, target):
    """Display every brute-force candidate and return the closest x value.

    Searches from -100.0 through 100.0 in increments of 0.1, printing each
    candidate, its predicted result, and its difference from the target.
    """
    best_x = -100.0
    smallest_difference = float("inf")

    for index in range(2001):
        x = -100.0 + index * 0.1
        predicted_result = a * x + b
        difference = abs(predicted_result - target)

        print(
            f"x = {x:.1f}, predicted result = {predicted_result:.2f}, "
            f"difference = {difference:.2f}"
        )

        # Preserve the first candidate in a tie by updating only for a smaller difference.
        if difference < smallest_difference:
            smallest_difference = difference
            best_x = x

    return best_x


def main():
    """Run the interactive smart calculator menu until the user exits."""
    while True:
        print("\nSmart Calculator")
        print("1. Basic calculation")
        print("2. Solve an equation")
        print("3. Visualize brute-force search")
        print("4. Learn about search methods")
        print("5. Exit")

        selection = input("Choose an option (1-5): ")

        if selection == "1":
            try:
                first_number = float(input("Enter the first number: "))
                operator = input("Enter an arithmetic operator (+, -, *, /): ")
                second_number = float(input("Enter the second number: "))
            except ValueError:
                print("Please enter valid numbers.")
                continue

            try:
                result = basic_calculate(first_number, operator, second_number)
            except ValueError as error:
                print(error)
                continue

            if result is None:
                print("Cannot divide by zero.")
            else:
                print(f"Result: {result}")
        elif selection == "2":
            equation_solver_menu()
        elif selection == "3":
            # Show all search attempts before reporting the closest candidate.
            best_x = visualize_search(1, 5, 12)
            print(f"Approximate solution: x = {best_x:.1f}")
        elif selection == "4":
            print(
                "Brute-force search checks candidates one at a time until it "
                "finds the closest solution. Testing 2,001 candidates can be "
                "slow because every candidate must be evaluated. For a "
                "monotonic function, binary search is smarter: it repeatedly "
                "narrows the search interval."
            )
        elif selection == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please choose an option from 1 to 5.")


if __name__ == "__main__":
    main()