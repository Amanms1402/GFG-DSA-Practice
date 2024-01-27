class Solution:
    def maxSubArraySum(self, arr, N):
        
        if N == 0:
            return 0

        max_sum = float('-inf')
        current_sum = 0

        for i in range(N):
            current_sum += arr[i]

            # Update max_sum if current_sum is greater
            if current_sum > max_sum:
                max_sum = current_sum

            # Reset current_sum to 0 if it becomes negative
            if current_sum < 0:
                current_sum = 0

        # If all elements are negative, return the maximum negative element
        if max_sum == float('-inf'):
            return max(arr)

        return max_sum
