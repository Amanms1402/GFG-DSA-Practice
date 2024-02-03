'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def decimalValue(self, head):
        MOD=10**9+7
        def lenght(head):
            curr=head
            l=0
            while(curr!=None):
                l+=1
                curr=curr.next
            return l
        curr=head
        ans=0
        l1=lenght(head)-1
        while(curr!=None):
            ans+=((2**l1)*curr.data)
            l1-=1
            curr=curr.next
        return ans%MOD
