class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Return an empty array if the number of elements in original != product of max dimensions
        if m*n != len(original):
            return []
        
        # Create an Empty array
        newArray = []

        #Add all the elements
        for i in range(0, len(original), n):
            newArray.append(original[i:i+n])

        # Return m x n 2D array constructed.
        return newArray
