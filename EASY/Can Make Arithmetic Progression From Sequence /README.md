# Question
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers ```arr```, return ```true``` if the array can be rearranged to form an arithmetic progression. Otherwise, return ```false```.

# Approach

1. Sort the array ```arr```.
2. Run the loop from ```0``` to ```len(arr)-2```
3. Continue the loop if this condition is met: ``` arr[i+2]-arr[i+1] == arr[i+1]-arr[i] ```, Else return ```False``` if the condition isn't met.
4. Return ```True``` on completion of the loop.
