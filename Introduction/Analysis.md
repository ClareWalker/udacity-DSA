Note: For this analysis, we will denote
 - nc = number of calls, i.e. len(calls)
 - nt = number of texts, i.e. len(texts)
 - n  = number of records, i.e. nc + nt

Task 0

The algorithm prints the first item in calls and text list, regardless of the number of
items in each list. So the algorithm takes 2.

he Big-O time complexity is O(1), i.e. constant.


Task 1

The algorithm iterates through each item in calls and texts. Each iteration executes two
set addition tasks (one per incoming and receiving). As seen_numbers is a set, the
time complexity of set addition is O(1).

The Big-0 time complexity is O(n), i.e. linear


Task 2

The algorithm has two parts: creating the dictionary mapping numbers to total call
duration & iterating through this dictionary to find the number with the longest call
time.

The first part executes 4 tasks for each call (if statement and increasing total duration
for each of incoming and receiving numbers: 2 * 2 = 4), so takes nc*4.

The second part iterates through all unique numbers. In the worst case, the dictionary
is sorted in reverse, so each iteration takes 3 tasks (if statement, assignment of
max_number, assignment of max_duration). If we let nc_unique be count of unique numbers
in calls, then it takes nc_unique*3. In the worst case, each calling and receiving
number is unique, so nc_unique = 2*nc and the second part takes nc*6.

Overall, it takes nc*4 + nc*6 = nc*10.

The Big-O time complexity is O(nc), i.e. linear in terms of number of calls (nc)


Task 3

There are four components to this algorithm: creating the dictionary mapping area codes
to number of times called by Bangalore, sorting the unique receiving codes in lexicographic
order, printing the ordered codes, calculate and print the percentage.

The first part takes 5 tasks per call from Bangalore and 1 task per call from elsewhere.
In the worst case all calls come from Bangalore, so it takes nc*5.

The second part uses built-in list.sort() to sort unique area codes. Being an implementation
of Samplesort it has worst-case time-complexity of O(n*logn) where n is the number of
unique codes. In the worst-case, each call is made to a unique code so n = nc.

The time taken by the third and last part does not depend on the number of calls.

Overall, it takes nc*5 + nc*log(nc)*a + nc + b where a and b are constants.
nc*log(nc) > nc.

The Big-O time complexity is O(n*log(n)), i.e. log-linear in the number of calls (nc).


Task 4

The algorithm has four parts: creating sets of numbers that are possible telemarketers
and those not telemarketers, calculating the difference between sets, sorting remaining
possible telemarketers, printing possible telemarketers.

Similar to previous tasks, if we assume worst-case of all unique numbers, the first part
takes n*4 = nc*4 + nt*4 and the second part takes nc*2 as time complexity of s1 - s2 is
O(len(s1)).

The third part again uses the builtin sorted() on possible telemarketers, which has log-linear
time complexity, O(nclog(nc)).

The last part is constant, O(1).

Overall, the algorithm takes nt*4 + nc*7 + a*nc*log(nc).

The Big-O time complexity is log-linear in the number of calls (nc) and linear in
the number of texts (nt).








