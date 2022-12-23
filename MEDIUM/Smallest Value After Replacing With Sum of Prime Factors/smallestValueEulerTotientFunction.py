class Solution:
    def smallestValue(self, n: int) -> int:
        
        def helper(n):
            ans = 0
            
            while n % 2 == 0:
                ans += 2
                n = n // 2
                
            for i in range(3, math.isqrt(n) + 1, 2):
                while n % i == 0:
                    ans += i
                    n = n // i
                    
            if n > 2:
                ans += n
                
            return ans
        
        got = helper(n)        
        while got != n:
            n = got
            got = helper(got)
            
        return got
        
