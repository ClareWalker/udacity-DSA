Explanation:

To find the floored square root of a number, we can use a binary search approach. This is optimal as it runs in O(log(n)) time as desired.

Time complexity:

Given we're using binary search, the time complexity of this solution is O(log(n)), where log is base 2.
The logarithmic behavior arises from the fact that we can divide the search space in half at each step. In each comparison, the search space is reduced by a factor of 2. The logarithm base 2 of n represents the number of times we can divide n by 2 until we reach 1. 

Space complexity:

The space complexity is O(1) as we are using only a constant amount of additional space.