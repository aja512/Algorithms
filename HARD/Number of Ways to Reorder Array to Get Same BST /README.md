# Question
[1569. Number of Ways to Reorder Array to Get Same BST](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/description/)

Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.

For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.
Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.

Since the answer may be very large, return it modulo 10<sup>9</sup> + 7.

# Intuition
Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.

The code works as follows:
1. It first defines a function ```cnr()``` that calculates the combination of two numbers. This function is used later in the code to calculate the number of ways to split a range of numbers into two smaller ranges.

2. It then defines two arrays, ```leng``` and ```cnt```, which store the length and count of each range of numbers, respectively.

3. It then iterates through the array ```nums``` in reverse order. For each number ```p```, it calculates the length of the range of numbers to the left of ```p``` (stored in ```h```) and the length of the range of numbers to the right of ```p``` (stored in ```k```).

4. It then calculates the number of ways to split the range of numbers from ```p-h``` to ```p+k``` into two smaller ranges. This is done by multiplying the count of the range of numbers to the left of ```p``` (stored in ```cnt[p-1]```), the count of the range of numbers to the right of ```p``` (stored in ```cnt[p+1]```), and the combination of ```h+k``` and ```h```.

5. It then updates the length and count of the range of numbers from ```p-h``` to ```p+k``` to be ```h+k+1``` and ```t```, respectively.

6. It repeats steps 3-5 for each number in ```nums```.

7. It then returns the count of the range of numbers from ```1 to n```, which is stored in ```cnt[1]```.




# Approach
Use bottom-up recursion with merge interval.

# Complexity
## Time complexity:
$$O(n^2)$$ 
- This is because the code iterates through the array nums once, and for each number in the array, it calculates the length and count of the range of numbers to the left and right of the number.

## Space complexity:
$$O(n^2)$$

This is because the two arrays leng and cnt both have a size of n+2, and each element in the arrays takes up constant space. Therefore, the total space complexity is O(n<sup>2</sup>).
Here is a breakdown of the space complexity of each of the two arrays:

- leng: This array stores the lengths of the intervals that have been processed so far. The size of this array is n+2 because we need to store the lengths of all intervals, including the empty interval at the beginning and end.
    
- cnt: This array stores the number of ways to partition the intervals that have been processed so far. The size of this array is also n+2 because we need to store the number of ways to partition all intervals, including the empty partition at the beginning and end.


The total space complexity is then the sum of the space complexities of the two arrays, which is O(n<sup>2</sup>).
