def get_min_max(ints):
    if len(ints) == 0:
        return None

    minimum = maximum = ints[0]

    for num in ints[1:]:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num

    return minimum, maximum

# Test cases
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Additional test cases

# Test Case 1: Empty array
print(get_min_max([]))
# Expected output: None

# Test Case 2: Array with a single element
print(get_min_max([5]))
# Expected output: (5, 5)

# Test Case 3: Array with duplicate elements
print(get_min_max([7, 2, 9, 2, 5, 1, 8, 5]))
# Expected output: (1, 9)

# Test Case 4: Large array
large_array = list(range(1, 10**6 + 1))
random.shuffle(large_array)
print(get_min_max(large_array))
# Expected output: (1, 1000000)