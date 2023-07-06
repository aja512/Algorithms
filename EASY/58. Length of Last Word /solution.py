class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        i, count = len(s) - 1, 0

        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            count += 1
            i -= 1

        return count
