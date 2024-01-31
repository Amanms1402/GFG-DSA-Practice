class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        if not head or head.next==None:
            return False
            
            
        s=set()
        while head:
            
            
            if head in s:
                return True
                
            s.add(head)
            
            head=head.next
            
            
        return False
