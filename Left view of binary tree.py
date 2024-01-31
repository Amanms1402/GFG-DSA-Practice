def LeftView(root):
    
    # code here
    if root is None:
        return []
        
    ans = []
    q = []
    q.append(root)
    while len(q)!=0:
        count = len(q)
        for i in range(count):
            curr = q[0]
            q.pop(0)
            if i==0:
                 ans.append(curr.data)
            
            
            
            if curr.left is not None:
                  q.append(curr.left)
            
            if curr.right is not None:
                   q.append(curr.right)
            
    return ans