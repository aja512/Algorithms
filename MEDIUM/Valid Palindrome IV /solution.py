class Solution:
    def makePalindrome(self, s: str) -> bool:
        res = []
        if s == s[::-1]:
            return True
        for i, j in zip(s,s[::-1]):
            if i != j and [j,i] not in res:
                res.append([i,j])
            if len(res) > 2:
                return False
        return True 
        
