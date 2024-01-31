class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        prev = Node(0)
        prev.next = head
        arr = set()
        curr = head
        while curr:
            if curr in arr:
                prev.next = None
                break
            arr.add(curr)
            curr = curr.next
            prev= prev.next
        return head