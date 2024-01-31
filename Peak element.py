class Solution:
    def peakElement(self, arr, n):
        start = 0
        end = n - 1
        
        while start <= end:
            mid = (start + end) // 2

            # If both indices are the same
            if start == end:
                return start

            # If mid is at the 0th index
            if mid == 0:
                if arr[mid] < arr[mid + 1]:
                    return mid + 1
                return mid

            elif arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid

            elif arr[mid] > arr[mid - 1] and arr[mid] == arr[mid + 1]:
                return mid

            elif arr[mid] > arr[mid - 1] and arr[mid] < arr[mid + 1]:
                start = mid + 1

            elif arr[mid] == arr[mid - 1] and arr[mid] < arr[mid + 1]:
                start = mid + 1

            else:
                end = mid - 1

        return 0