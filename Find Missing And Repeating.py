class Solution:
    def findTwoElement(self, arr, n): 
        sumarr = sum(arr)
        exsum = (n * (n+1))/2
        
        for j in range(n):
            if (arr[abs(arr[j])-1] < 0):
                rep = abs(arr[j])
                break
            else:
                arr[abs(arr[j])-1] = arr[abs(arr[j])-1] * (-1)
                
        sumarr = sumarr - rep
        miss = int(exsum - sumarr)
        
        return [rep, miss]
