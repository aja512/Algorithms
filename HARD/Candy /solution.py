class Solution:
    def check_candies(self, ratings:List[int], candies:List[int]) -> bool:
        for i, value in enumerate(ratings[1:-1]):
            index = i + 1
            if ratings[index] > ratings[index-1] and candies[index] <= candies[index-1]:
                return True
            if ratings[index] > ratings[index+1] and candies[index] <= candies[index+1]:
                return True
        if ratings[0] > ratings[1] and candies[0] <= candies[1]:
            return True
        if ratings[-1] > ratings[-2] and candies[-1] <= candies[-2]:
            return True
        return False

    def candy(self, ratings: List[int]) -> int: 
        n=len(ratings)
        temp = [1]*n
        
        for i in range(1,n):
            if(ratings[i]>ratings[i-1]):
                temp[i]=temp[i-1]+1
        if(n>1):
            if(ratings[0]>ratings[1]):
                temp[0]=2
                
            
        for i in range(n-2,-1,-1):
            if(ratings[i]>ratings[i+1] and temp[i]<=temp[i+1]):
                temp[i]=temp[i+1]+1

                
        return sum(temp) 
