# Question
Given two integer arrays ```arr1``` and ```arr2```, return the minimum number of operations (possibly zero) needed to make ```arr1``` strictly increasing.

In one operation, you can choose two indices ```0 <= i < arr1.length``` and ```0 <= j < arr2.length``` and do the assignment ```arr1[i] = arr2[j]```.

If there is no way to make arr1 strictly increasing, return ```-1```.

# Approach

The code first imports the `bisect` module, which provides a number of functions for working with sorted lists. The `arr2` array is then sorted and the unique elements are extracted using the `set()` function. The lengths of the two arrays are then stored in the variables `n1` and `n2`.

A dictionary `d` is then created, which maps the number of operations needed to make `arr1` strictly increasing to the value of the last element that was swapped. The initial value of the dictionary is `{0: arr1[0]}`, which means that no operations are needed to make the first element of `arr1` increasing. If the first element of `arr2` is less than the first element of `arr1`, then the value `1` is added to the dictionary with the value of the first element of `arr2`.

For each element `x` in `arr1`, a new dictionary `new_d` is created. The values in `d` are then checked to see if they are less than `x`. If they are, then they are added to `new_d`. The values in `d` are also checked to see if they are in `arr2`. If they are, then the index of the value in `arr2` is found using the `bisect.bisect_right()` function. If the index is less than `n2`, then the value at the index is added to `new_d` if it is not already present.

The `d` dictionary is then updated with the values from `new_d`. This process is repeated for each element in `arr1`.

If the `d` dictionary is not empty, then the minimum number of operations needed to make `arr1` strictly increasing is returned. Otherwise, `-1` is returned.

Here is a more detailed explanation of the code:
```
import bisect
```

## Sort the arr2 array and extract the unique elements.
```
arr2 = sorted(set(arr2))
```

## Get the lengths of the two arrays.
```
n1, n2 = len(arr1), len(arr2)
```

## Create a dictionary that maps the number of operations needed to make arr1 strictly increasing to the value of the last element that was swapped.
```
d = {0: arr1[0]}
if arr2[0] < arr1[0]:
    d[1] = arr2[0]
 ```   

## For each element in arr1, check if the values in d are less than it. If they are, add them to a new dictionary. Also check if the values in d are in arr2. If they are, find the index of the value in arr2 and add it to the new dictionary if it is not already present.
```
for i in range(1, n1):
    new_d = {}
    x = arr1[i]
    for time, value in d.items():
        if value < x:
            new_d[time] = x
    for time, value in d.items():
        index = bisect.bisect_right(arr2, value)
        if index < n2:
            if time + 1 in new_d:
                new_d[time + 1] = min(new_d[time + 1], arr2[index])
            else:
                new_d[time + 1] = arr2[index]
```                

## Update the d dictionary with the values from the new dictionary.
```
    d = new_d 
```

## If the d dictionary is not empty, return the minimum number of operations needed to make arr1 strictly increasing. Otherwise, return -1.
```
if d:
    return min(d.keys())
return -1
```
