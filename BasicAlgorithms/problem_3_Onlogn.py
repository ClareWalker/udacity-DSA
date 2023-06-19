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

    # Convert the input list to a max heap
    max_heapify(input_list)

    # Build two numbers by alternately selecting elements from the max heap
    num1 = 0
    num2 = 0
    add_to_num1 = True

    while len(input_list) > 0:
        if add_to_num1:
            num1 = num1 * 10 + input_list[0]
        else:
            num2 = num2 * 10 + input_list[0]

        # Remove used digit from heap
        input_list.pop(0)
        # Move new first digit to correct place in heap
        sift_down(input_list, 0)
        add_to_num1 = not add_to_num1

    return [num1, num2]


def max_heapify(arr):
    # Convert the input list to a max heap using bottom-up approach
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, i)


def sift_down(arr, i):
    # Sift down the element at index i in the max heap
    n = len(arr)
    largest = i
    left_child = (2 * i) + 1
    right_child = (2 * i) + 2

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # Check if a child is larger than element at i
    if largest != i:
        # if so, swap child with element
        arr[i], arr[largest] = arr[largest], arr[i]
        # continue recursively, now with the element in place of largest child
        sift_down(arr, largest)

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


