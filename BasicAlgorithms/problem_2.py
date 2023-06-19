def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if not input_list or not number:
        return -1

    start = 0
    end = len(input_list) - 1

    while start <= end:
        mid = (start + end) // 2

        if input_list[mid] == number:
            return mid

        if input_list[start] <= input_list[mid]:
            # Check whether number is in segment: start - mid
            if input_list[start] <= number <= input_list[mid]:
                # If yes, reduce search space to this segment
                end = mid - 1
            else:
                # If not, reduce search space to segment: mid - end
                start = mid + 1
        else:
            if input_list[mid] <= number <= input_list[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1


def linear_search(input_list, number):
    if input_list is None:
        return -1

    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# Test Cases
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Additional Test Cases
# Test Case 1: Empty input list
test_function([[], 6])
# Pass: The input list is empty. The function correctly returns -1.

# Test Case 2: Null input list
test_function([None, 6])
# Pass: The input list is null. The function correctly returns -1.

# Test Case 3: Large input list
test_function([[i for i in range(10**6)], 999])
# Pass: The input list is a sorted array from 0 to 999999. The target value 999999 is found at index 999999. The function correctly returns the index.
