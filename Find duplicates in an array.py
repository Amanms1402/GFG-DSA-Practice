class Solution:
    def duplicates(self, arr, n):
        # Create a temporary list to track visited elements
        visited = [-1 for _ in range(n)]
       
        # Iterate through the input list
        for element in arr:
            # If the element has not been visited yet
            if visited[element] == -1:
                visited[element] = -10
            # If the element has been visited once before
            elif visited[element] == -10:
                visited[element] = element
       
        # Initialize a position pointer
        pos = 0
       
        # Reconstruct the input list with unique elements
        for i in range(n):
            if visited[i] > -1:
                arr[pos] = i
                pos += 1
       
        # If there are no unique elements, return [-1]
        if not pos:
            return [-1]
       
        # Remove any extra elements from the end of the list
        for i in range(pos, n):
            arr.pop()
       
        return arr