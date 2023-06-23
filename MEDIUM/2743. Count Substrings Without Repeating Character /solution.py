class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        
        n, left, seen = len(s), 0, set()
        ans = n*(n+1)//2     # pre-adding the "right+1" part           
        
        for ch in s:
            
            while ch in seen:
                seen.remove(s[left])
                left+= 1

            seen.add(ch)
            ans-= left

        return ans
