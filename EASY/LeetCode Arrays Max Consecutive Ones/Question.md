# Question:
[Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/)

# Hint 1
You need to think about two things as far as any window is concerned. One is the starting point for the window. 
How do you detect that a new window of 1s has started? The next part is detecting the ending point for this window. 
How do you detect the ending point for an existing window? If you figure these two things out, you will be able to detect the windows of consecutive ones. All that remains afterward is to find the longest such window and return the size.
