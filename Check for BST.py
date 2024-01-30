class Solution:
    def isBST(self, root):
        def ok(node,left=-float('inf'),right=float('inf')):
            if not left<node.data<right:
                return False
            leftok=True if not node.left else ok(node.left,left,node.data)
            rightok=True if not node.right else ok(node.right,node.data,right)
            return leftok and rightok
        return ok(root)