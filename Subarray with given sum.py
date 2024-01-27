class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
        l=r=curr_sum=0
        if sum(arr) < s or (s == 0 and 0 not in arr): return [-1]
            
            
        while l<=r:
            if curr_sum < s:
                if r >=n: return [-1]
                curr_sum+=arr[r]
                r+=1
            if curr_sum > s:
                curr_sum-=arr[l]
                l+=1
            if curr_sum == s:
                if r==0:
                    return(1,1)
                return (l+1,r)
        return [-1]