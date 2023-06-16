class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 1000000007
        n = len(nums)


        # stores the length of each range of numbers, respectively.
        leng = [0]*(n+2) 

        # stores the count of each range of numbers, respectively.
        cnt = [1]*(n+2) 

        # Iterate the array in reverse order
        for p in nums[::-1]: 
            
            # For each number p, it calculates the length of the range of numbers to the left of p (stored in h) and the length of the range of numbers to the right of p (stored in k).  
            h,k = leng[p-1],leng[p+1] 

            # Calculates the number of ways to split the range of numbers from p-h to p+k into two smaller ranges. This is done by multiplying the count of the range of numbers to the left of p (stored in cnt[p-1]), the count of the range of numbers to the right of p (stored in cnt[p+1]), and the combination of h+k and h
            t = (cnt[p-1]*cnt[p+1]%mod)*comb(h+k,h)%mod 

            # update leng and cnt arrays
            leng[p-h]=leng[p+k]=h+k+1
            cnt[p-h]=cnt[p+k]=t

        # return the number of ways to reorder nums
        return (cnt[1]-1)%mod
            
            
