class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        count,dic=0,{}
        for i in range(n):
            if k-arr[i] in dic:
                count=count+dic[k-arr[i]]
            dic[arr[i]]=dic.get(arr[i],0)+1
        return count