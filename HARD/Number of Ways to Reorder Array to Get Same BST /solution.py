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
            # k consecutive values larger than p (on the left) are already in BST if leng[p+1] > 0 indicates that. Length [p+1] and h are the respective integers in the right child BST of p.
            h,k = leng[p-1],leng[p+1] 

            # The size of the BST rooted at p should be used to update the lengths at the rightmost and leftmost numbers in the BST (consecutive intervals). Because it won't be needed in the subsequent computation of length and cnt, the numbers in between (p-h, p+k) don't need to be updated.
            leng[p-h]=leng[p+k]=h+k+1 

            # The number of permutated arrays that can construct the BST of the left child and the right child of p is given by dp(BST rooted at p) = dp(left(p-1))*dp(right(p+1))*C(left+right,right).
            t = (cnt[p-1]*cnt[p+1]%mod)*comb(h+k,h)%mod 

            # Only the cnt's rightmost and leftmost elements should be updated because those two numbers will be the only ones used in the next merge interval.
            cnt[p-h]=cnt[p+k]=t 

            # return the number of ways to reorder nums
        return (cnt[1]-1)%mod
            
            
