class Solution:
    def binarysearch(self, arr, n, k):
        # code here
        for i in range(0, n):
            if arr[i] == k:
                return i
        return -1