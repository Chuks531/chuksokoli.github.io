import re

def MissingDigit(equation: str) -> int:
    # Step 1: Split the equation at '='
    left, right = equation.split("=")
    left, right = left.strip(), right.strip()

    # Step 2: Extract the parts of the left-hand side
    match = re.match(r"(\S+)\s*([\+\-\*/])\s*(\S+)", left)
    if not match:
        return -1  # Return error if parsing fails
    
    num1, operator, num2 = match.groups()
    num1, num2, right = num1.strip(), num2.strip(), right.strip()

    # Step 3: Find the missing digit (in num1, num2, or right)
    for digit in range(10):  # Test digits 0-9
        # Replace 'x' with the digit in all parts
        test_num1 = num1.replace("x", str(digit))
        test_num2 = num2.replace("x", str(digit))
        test_right = right.replace("x", str(digit))

        # Ensure valid integer format (avoid cases like "03")
        if test_num1.isdigit() and test_num2.isdigit() and test_right.isdigit():
            # Convert all numbers to integers
            val1, val2, expected_result = int(test_num1), int(test_num2), int(test_right)

            # Step 4: Check if the equation holds
            if operator == "+" and val1 + val2 == expected_result:
                return digit
            elif operator == "-" and val1 - val2 == expected_result:
                return digit
            elif operator == "*" and val1 * val2 == expected_result:
                return digit
            elif operator == "/" and val2 != 0 and val1 // val2 == expected_result:
                return digit

    return -1  # No valid digit found (should never happen per problem constraints)

# ✅ Test Cases
print(MissingDigit("4 - 2 = x"))  # Output: 2
print(MissingDigit("1x0 * 12 = 1200"))  # Output: 0
print(MissingDigit("3x + 12 = 46"))  # Output: 4
print(MissingDigit("8 * x = 40"))  # Output: 5
