class Solution:
     def subLinkedList(self, l1, l2): 
        # Code here
        # return head of difference list
        
        def make_number(head):
            c=0
            cur=head
            while(cur):
                c=c*10+cur.data
                cur=cur.next
            return c
        
        a1=make_number(l1)
        a2=make_number(l2)
        a3=Node(abs(a1-a2))
        return a3