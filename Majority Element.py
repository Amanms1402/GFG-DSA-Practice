class Solution:
    def majorityElement(self, A, N):
        #Your code here
        #voting algorithm
        count = 1
        maj = A[0]
        
        if N ==1:
            return A[0]
        
        for i in A[1:]:
            if maj == i: # if same number
                count+=1
            else: # if different number
                count -=1  
                
            if count == 0: # changing the majority element
                count = 1
                maj = i
    
        
        # counting the occurance of Maj Element.
        check_counter = 0
        for i in A:
            if i == maj:
                check_counter +=1
            
        # checking majority element is gt N/2
        if check_counter > N/2:
            return maj
                
                
        return -1