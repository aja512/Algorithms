# Question
You are given two 0-indexed arrays `nums` and `cost` consisting each of `n` positive integers.

You can do the following operation any number of times: Increase or decrease any element of the array `nums` by `1`.

The cost of doing one operation on the `ith` element is `cost[i]`.

Return the minimum total cost such that all the elements of the array `nums` become equal.

# Intuition
Since it asked to perform some operation (i.e. increasse/decrease elements by 1), it would be best to use mean of all elements belonging to `cost`. So using the hints we need to perform Iterative traversal and update

# Approach
1. Sort the elements.
2. Determine the mean of `cost`.
3. Create a new variable `count` and set it to `0`.
4. Iterater through your 2D array containing nums and cost.
5. Add the `cost[i]` to `count`.
6. If `count>= mid`, return the positive value of `(target-n)*c` from the elements in array
7. Repat Steps 5 and 6 till full traversal done

# Complexity
- Time complexity: $$O(nlog(n))$$ 

- Space complexity: $$O(n)$$
