# Question
You are given an array ```coordinates```, ```coordinates[i] = [x, y]```, where ```[x, y]``` represents the coordinate of a point. 
Check if these points make a straight line in the XY plane.

# Approach
Use the formula for slope and y-coordinates

```
For list of coordinates
  if i[0] * m + b != i[1]:
    return False

return True
 ```
       
