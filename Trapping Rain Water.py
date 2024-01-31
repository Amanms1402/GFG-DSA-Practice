class Solution:
    def trappingWater(self, arr,n):
        #Code here
        maxLeft = [0]
        ml = 0
        maxRight = [0] 
        mr = 0
        ans = 0
        TotalMin = 0
        n = len(arr)
        if n <= 2:
            return 0
            
        for i in range(1, n):
            ml = max(arr[i-1], ml)
            maxLeft.append(ml)
            
        for i in range(n - 2, -1, -1):
            mr = max(arr[i+1], mr)
            maxRight.append(mr)
        maxRight = maxRight[::-1]
        
        for i in range(1, n-1):
            TotalMin = min(maxLeft[i], maxRight[i])
            ans += max(0, TotalMin - arr[i])
        return ans