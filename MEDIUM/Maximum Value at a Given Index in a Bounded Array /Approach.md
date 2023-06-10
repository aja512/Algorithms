The optimal array always have the form ```..., amax - 2, amax - 1, amax, amax -1, amax - 2, amax - 3, ...```, where ```a_index = amax```. And, if you plot the array in 2D, it is always in a pyramid shape. The area under the curve is the sum of the array. The only tricky thing is the boundaries.

Depending on the maxSum, there are 3 cases.

1. The first case is that the maxSum is small enough so that the shape is a perfect symmetric pyramid. In this case, the area of a given pyramid height h is h^2. So given a area = maxSum, the max height is h = sqrt(maxSum).
2. The second case is that the pyramid already hit the right bounday but not the left boundary (or vice versa). The solution requires one to solve a quadratic equation, i.e. x = (-b + sqrt(b^2 -4ac)) / (2a).
3. The third case is that the pyramid is tall enogh to hit both boundaries. In this case, one can just subtract the maximum area computed in case 2. The the remaining height is simply (remaining_max_sum // n).

Now, if you are really into this math solution, here is how I get the formula for case 2:
The largest allowed ```maxSum``` for the second case is when the left side is a perfect triangle (which will take ```tri_left``` area), and the right side is a triangle on top of a rectangle, which have ```tri_right``` and ```(n_left - n_right) * n_right``` areas, respectively. The center bar at index will take ```n_left + 1``` area. So that gives the largest allowed maxSum to be

```
(tri_left + tri_right + (n_left - n_right) * n_right + n_left + 1)
```

If ```maxSum``` is larger than this, the left side will be a triangle also on top of a rectangle, which becomes the case 3.

To figure out the solution, it is the same formula as the condition equaion. But you want to allow the left triangle to have a unknown width ```l``` (and height). Let's say the center bar have height ```h = l + 1```. The total area (which will be ```maxSum```) will be

```
A = left_triangle_area(l) + tri_right + (l - n_right) * n_right + h
```

where ```l = h - 1``` is the unknown width of the left triangle, and ```left_triangle_area(h) = l * (l + 1) / 2``` is a function of ```l```. So this becomes a quadratic equation on ```l```:

```
maxSum = (l^2 + l) / 2 + tri_right + (l - n_right) * n_right + l + 1
```

Multiplying both sides by 2 and putting it into the standard quadratic equation form ```a * x^2 +b * x + c = 0```, we get

```
l^2 + (3 + 2 * n_right) * l + 2 * (tri_right + 1 - n_right * n_right - maxSum) = 0
```

so

```
a = 1
b = (3 + 2 * n_right)
c = 2 * (tri_right + 1 - n_right * n_right - maxSum)
```

Then using the quadratic formula, one get the solution to the height is

```
h = l + 1 = (-b + sqrt(b^2 -4ac)) / (2a) + 1
```
We add another 1 because we subtracted it at the beginning.

