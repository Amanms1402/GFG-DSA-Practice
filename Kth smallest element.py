class Solution:
    @staticmethod
    def kthSmallest(arr, l, r, k):
        # Your code here
        arr.sort()
        return arr[l + k - 1]