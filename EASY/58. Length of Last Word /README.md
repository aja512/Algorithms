# Question

Given a string `s` consisting of words and spaces, return the length of the **last** word in the string.

A **word** is a maximal substring consisting of non-space characters only.

[LeetCode 58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/)

# Approach:
1. Count from the reverse.
2. If we see a blank space, move the pointer to the right.
3. If we see a character, increment the count.
