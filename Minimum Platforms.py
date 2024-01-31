class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        count=1
        max=1
        i=1
        j=0
        while i<n and j<n:
            if arr[i]<=dep[j]:
                i+=1
                count+=1
                if count> max:
                    max=count
            else:
                j+=1
                count-=1
        return max