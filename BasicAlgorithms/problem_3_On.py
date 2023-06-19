def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two numbers such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None or len(input_list) < 2:
        return []

    # Count the frequency of each digit in the input list
    digit_counts = [0] * 10
    for digit in input_list:
        digit_counts[digit] += 1

    # Construct the two numbers by arranging the digits in descending order
    num1 = ""
    num2 = ""
    # Start by adding to first number, then iterate
    add_to_num1 = True

    for i in range(9, -1, -1):
        count = digit_counts[i]

        while count > 0:
            if add_to_num1:
                num1 += str(i)
            else:
                num2 += str(i)

            add_to_num1 = not add_to_num1
            count -= 1

    return [int(num1), int(num2)]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Test cases
test_function([[1, 2, 3, 4, 5], [542, 31]])
# Pass: The maximum sums that can be formed are [542, 31].

test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
# Pass: The maximum sums that can be formed are [964, 852].


# Additional Test Cases

# Test Case 1: Empty input list
test_function([[], []])
# Pass: The input list is empty. The function correctly returns an empty list.

# Test Case 2: Null input list
test_function([None, []])
# Pass: The input list is null. The function correctly returns an empty list.

# Test Case 3: Large input list

test_function([[9] * 100, [99999999999999999999999999999999999999999999999999,
                           99999999999999999999999999999999999999999999999999]])
# Pass: The answer builds up two numbers of repeated 9's, each with 50 digits
print([len(str(d)) for d in rearrange_digits([9] * 100)])
# Expected output: [50, 50]



