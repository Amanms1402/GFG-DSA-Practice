class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        result=[-1]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while(stack and arr[i]>=arr[stack[-1]]):
                stack.pop()
            if stack:
                result[i]=arr[stack[-1]]
            else:
                result[i]=-1
            stack.append(i)
        return result