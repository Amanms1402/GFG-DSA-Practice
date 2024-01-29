class Solution:
    def minJumps(self, arr, n):
        #code here
        idx = 0
        d = 0
        nn = n
        while True:
            val = arr[idx]
            # First filter
            if val == 0: return -1
            if (len(arr) == 1): break
        
            # Get the range value
            temp_val = arr[idx+1:val+idx+1]
            
            # If the current idx + val more than enough, get one step
            if (idx + val >= n-1):
                d+=1
                break
            
            # Sort by tuple
            val, i = max((v+i, i) for i, v in enumerate(temp_val))
            
            # If this enough to be more than the val, then add 2 steps.
            if idx + (val-i) >= n-1:
                d+=2
                break
            # Else, move forward to the next index.
            else:
                idx += (i+1)
                d+=1
            
        return d