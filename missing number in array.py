class Solution:
    def missingNumber(self,array,n):
        # code here
        return ((n)*(n+1)//2) - sum(array)