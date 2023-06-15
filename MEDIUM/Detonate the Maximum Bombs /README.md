# Question
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. 
This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array ```bombs``` where ```bombs[i] = [xi, yi, ri]```. ```xi``` and ```yi``` denote the X-coordinate and Y-coordinate of the location of the ```ith``` bomb, whereas ```ri``` denotes the ```radius``` of its range.

You may choose to detonate a single bomb. 
When a bomb is detonated, it will detonate all bombs that lie in its range. 
These bombs will further detonate the bombs that lie in their ranges.

Given the list of ```bombs```, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

# Approach
Use DFS to find the largest path in graph. Find largest path - run DFS from each node that has potential to detonate others. Return maxDetonated node.

## Conditions:
* If center of bomb[i] belongs to the range of bomb[j] => bomb[j] will detonate bomb[i]. 
* If center of bomb[j] belongs to the range of bomb[i] ==> bomb[i] will detonate bomb[j].

Perform DFS on visited and BombID

```
def dfs(bombID, visited):
  visited.add(bombID)
  for nei in g[bombID]:
    if nei not in visited:
      dfs(nei,visited)
 ```
 
[Detonate Maximum Bombs Question](https://leetcode.com/problems/detonate-the-maximum-bombs/)
