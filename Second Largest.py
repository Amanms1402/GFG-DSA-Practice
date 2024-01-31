class Solution:

	def print2largest(self,arr, n):
		# code here
		arr=list(set(arr))
		arr.sort()
		if len(arr)==1:
		    return -1
		return arr[-2]