# Given an array of sorted numbers, move all non-duplicate number instances at the beginning of the array in-place. The non-duplicate numbers should be sorted 
# you should not use any extra space so that the solution has constant space complexity
class Solution:
  def moveElements(self, arr):
    # Initialize the index for the next non-duplicate element
    next_non_duplicate = 1

    # Initialize the main loop index
    i = 0

    # Iterate through the array
    while i < len(arr):
      # Check if the current element is different from the previous element
      if arr[next_non_duplicate - 1] != arr[i]:
        # If different, update the next_non_duplicate element and copy the current element
        arr[next_non_duplicate] = arr[i]

        # Increment the next_non_duplicate index, only increments if next non dup = arr[i]
        next_non_duplicate += 1

      # Increment the main loop index
      i += 1

    # Return the length of the modified array as the result
    return next_non_duplicate

# Entry point of the program
def main():
  # Create an instance of the Solution class
  sol = Solution()

  # Test the 'moveElements' method with example arrays
  print(sol.moveElements([2, 3, 3, 3, 6, 9, 9]))  # Output: 4 (modified array: [2, 3, 6, 9, 6, 9, 9])
  print(sol.moveElements([2, 2, 2, 11]))         # Output: 2 (modified array: [2, 11, 2, 11])

# Execute the main function
main()