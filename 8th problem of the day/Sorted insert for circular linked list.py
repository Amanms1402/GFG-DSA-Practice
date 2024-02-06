class Solution:
  def sortedInsert(self, head, data):
    if not head:
        temp=Node(data)
        temp.next=temp
        return temp
    if head.data>data:
        temp=Node(head.data)
        temp.next=head.next
        head.next=temp
        head.data=data
    else:
        curr=head
        while curr.next!=head and curr.next.data<data:
            curr=curr.next
        temp=Node(data)
        temp.next=curr.next
        curr.next=temp
    return head