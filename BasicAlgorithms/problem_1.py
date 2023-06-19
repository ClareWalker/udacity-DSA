def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored square root
    Returns:
       int: Floored Square Root
    """
    if number is None:
        return None

    if number < 0:
        raise ValueError("Square root is not defined for negative numbers")

    if number == 0:
        return 0

    # Initialize the boundaries for binary search
    start = 1
    end = number

    # Binary search to find the square root
    while start <= end:
        mid = (start + end) // 2

        # Check if mid*mid is equal to the number
        if mid * mid == number:
            return mid

        # If mid*mid is less than the number, search in the right half
        elif mid * mid < number:
            start = mid + 1
            ans = mid  # Update the potential result, the lower bound will be floor of root

        # If mid*mid is greater than the number, search in the left half
        else:
            end = mid - 1

    return ans  # Return the floored square root

# Test Cases
print("Pass" if (3 == sqrt(9)) else "Fail")  # Expected: Pass
print("Pass" if (0 == sqrt(0)) else "Fail")  # Expected: Pass
print("Pass" if (4 == sqrt(16)) else "Fail")  # Expected: Pass
print("Pass" if (1 == sqrt(1)) else "Fail")  # Expected: Pass
print("Pass" if (5 == sqrt(27)) else "Fail")  # Expected: Pass

# Additional Test Case
print("Pass" if (None is sqrt(None)) else "Fail")  # Expected: Pass
print("Pass" if (0 == sqrt(0)) else "Fail")  # Expected: Pass
print("Pass" if (9999 == sqrt(99990001)) else "Fail")  # Expected: Pass
