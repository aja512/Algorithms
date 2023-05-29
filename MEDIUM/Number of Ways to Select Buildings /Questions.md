You are given a 0-indexed binary string ```s``` which represents the types of buildings along a street where:

* ```s[i] = '0'``` denotes that the ith building is an office and
* ```s[i] = '1'``` denotes that the ith building is a restaurant.
As a city official, you would like to select 3 buildings for random inspection. However, to ensure variety, no two consecutive buildings out of the selected buildings can be of the same type.

For example, given ```s = "001101"```, we cannot select the ```1<sup>st</sup>```, ```3<sup>rd</sup>```, and ```5<sup>th</sup>``` buildings as that would form ```"011"``` which is not allowed due to having two consecutive buildings of the same type.
Return the number of valid ways to select 3 buildings.
