#User function Template for python3
'''
	Your task is to return the data stored in
	the nth node from end of linked list.
	
	Function Arguments: head (reference to head of the list), n (pos of node from end)
	Return Type: Integer or -1 if no such node exits.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
#Function to find the data of nth node from the end of a linked list
def getNthFromLast(head,n):
    #code here
    t=head
    k=head
    c=0
    while(t!=None):
        c+=1
        t=t.next
    if n <= 0 or n > c:
        return -1
    while((c-n)!=0):
        k=k.next
        c-=1
    if k!=None:
        return k.data
    return -1