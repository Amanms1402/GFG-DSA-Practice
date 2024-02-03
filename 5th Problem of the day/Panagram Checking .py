class Solution:
    def checkPangram(self,s):
        #code here
        a="abcdefghijklmnopqrstuvwxyz"
        c=("".join("".join(s.split()).split(','))).lower()
        if len(c)<26:
            return False
        else:
            for i in c:
                if i in a:
                    a=a[:a.index(i)]+a[a.index(i)+1:]
            if a=="":
                return True
            else:
                return False