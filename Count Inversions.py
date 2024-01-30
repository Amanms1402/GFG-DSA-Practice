class Solution:
    #User function Template for python3
    
    def countMerge(self,arr,l,m,r):
        left = arr[l:m+1]
        right = arr[m+1:r+1]
        res,i,j,k = 0,0,0,l
        while i < len(left) and j< len(right):
            if left[i] <= right[j]:
                arr[k]=left[i]
                i += 1
            else:
                arr[k]=right[j]
                j+=1
                res +=len(left)-i
            k += 1
            
        while i < len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j< len(right):
            arr[k]=right[j]
            j+=1
            k+=1
        return res
        
    def inversCount(self,arr,l,r):
        res = 0
        if(l<r):
            m = (l+r)//2
            res += self.inversCount(arr,l,m)
            res += self.inversCount(arr,m+1,r)
            res += self.countMerge(arr,l,m,r)
        return res
        
    def inversionCount(self,arr,n):
        l=0
        r = n-1
        r1 = self.inversCount(arr,l,r)
        return r1