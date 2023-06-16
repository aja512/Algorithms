class Solution:
    # dp(s) = dp(left)*dp(right)*C(n-1,left), left+right=n-1
    # O(n^2)
    # top down: split interval; bottom-up: merge interval
    def numOfWays(self, nums: List[int]) -> int:
        mod = 1000000007
        n = len(nums)
        '''
        # combination(n,r)
        def cnr(n,r):
            if r==0 or n==r: return 1
            return (cnr(n-1,r)+cnr(n-1,r-1))%mod
        '''

        leng = [0]*(n+2)
        cnt = [1]*(n+2)
        for p in nums[::-1]:
            h,k = leng[p-1],leng[p+1]
            t = (cnt[p-1]*cnt[p+1]%mod)*comb(h+k,h)%mod
            leng[p-h]=leng[p+k]=h+k+1
            cnt[p-h]=cnt[p+k]=t
        
        return (cnt[1]-1)%mod
            
