# Question
Given an array of strings ```words``` and a width ```maxWidth```, format the text such that each line has exactly ```maxWidth``` characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. 
Pad extra spaces ```' '``` when necessary so that each line has exactly ```maxWidth``` characters.

Extra spaces between words should be distributed as evenly as possible. 
If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

**Note:**
* A word is defined as a character sequence consisting of non-space characters only.
* Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
* The input array ```words``` contains at least one word.

# Approach
We'll build the result array line by line while iterating over words in the input. Whenever the current line gets too big, we'll appropriately format it and proceed with the next line until for loop is over. Last but not least, we'll need to left-justify the last line.

Time complexity :O(n)
There is just one for loop, which iterates over words provided as input.

Space complexity: O(n + l)
Where n is lenght of words, and l max length of words in one line. Worst case scenario l = n, which will add up to O(2n) but in asymptotic analysis we don't care about constants so final complexity is linear: O(n)

