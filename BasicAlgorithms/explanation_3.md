I implemented two solutions:
 - O(n * log(n)): this is less efficient, but achieves required time complexity. This generalises better.
 - O(n): simpler, more efficient solution leveraging property that all digits are 0-9

O(n)

Explanation:

The rearrange_digits function first counts the frequency of each digit in the input list using an array called digit_counts. Then, it constructs two numbers by arranging the digits in descending order. 
This is only possible as we know all numbers in list must be 0-9.
It alternates between adding digits to num1 and num2 to ensure that the difference in the number of digits between the two numbers is at most 1. Finally, it returns the two numbers as a list.

Time complexity:

The time complexity of the function is O(n), where n is the size of the input list. Counting the frequency of digits and constructing the numbers both require iterating over the input list once. The additional operations, such as appending to strings and converting strings to integers, have constant time complexity.

Space complexity:

The space complexity of the function is O(1). It uses a fixed-size array digit_counts to count the frequency of digits and two strings num1 and num2 to store the two numbers. The size of these data structures does not depend on the size of the input list. Therefore, the space complexity is constant.


O(n * log(n))

Explanation:

This solution utilizes a max heap to rearrange the elements of the input list. It first converts the input list into a max heap using a bottom-up approach. The max_heapify function is used to maintain the max heap property. Then, it constructs two numbers by alternately selecting elements from the max heap, similar to solution above.
While less efficient, this solution would generalise to input lists with digits larger than 9.

Time complexity:

The time complexity of the solution is O(log(n) * n). The O(log(n) factor comes from the process of building the max heap using the max_heapify operation. 
The max_heapify operation has a time complexity of O(log(n)) and is performed on each element in the input list. Since there are n elements in the list, the overall time complexity of building the max heap becomes O(log(n) * n).
After building the max heap, the extraction of elements to form the two numbers takes O(n) time, as each element is sifted down once. However, since the O(log(n)) factor dominates the time complexity, we can simplify the overall time complexity to O(log(n) * n).


Space complexity:

The space complexity is O(1) because the solution does not use any additional data structures that grow with the input size. 
The rearrangement is done in-place within the input list itself, and the space required for variables and recursive function calls is constant and does not depend on the input size.