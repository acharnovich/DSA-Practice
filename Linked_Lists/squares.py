# Problem: Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.
# Solution: takes a list as input, creates squares and adds them to a new list from least to greatest
class Solution:
  # O(n) time and space complexity
  def makeSquares(self, arr):
    # Get the length of the input array
    n = len(arr)
    
    # Create a list to store the squares, initialized with zeros
    squares = [0 for x in range(n)]
    # pointer that starts from the beginning 
    left = 0
    # pointer that starts at the end of the arr
    right = n - 1
    # stores the hight index of the arr
    highestIdx = n - 1

    while left <= right:
        # creates the square for the left pointer
        leftSquare = arr[left] * arr[left]
        # creates the square for the right pointer 
        rightSquare = arr[right] * arr[right]
        if leftSquare > rightSquare:
          # stores the leftsquare in the highest index of the squares list
          squares[highestIdx] = leftSquare
          # bumps left pointer by one 
          left += 1
        else:
          # otherwise it sets the right pointer equal to the highest index
          squares[highestIdx] = rightSquare
          # bumps right pointer down one
          right -= 1
        # In either case, decrease highestIdx by one to store next pointer
        highestIdx -= 1

          
    
    # Return the resulting list of squares
    return squares
  
  # Easier solutuion, but has O(n * logN) time complexity 
  def makeSquaresEasy(self, nums):
    return sorted([num**2 for num in nums])



def main():
  sol = Solution()
  # Test the makeSquares method with example inputs
  print("Squares: " + str(sol.makeSquares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(sol.makeSquares([-3, -1, 0, 1, 2])))

  #print("Squares: " + str(sol.makeSquaresEasy([-2, -1, 0, 2, 3])))
  #print("Squares: " + str(sol.makeSquaresEasy([-3, -1, 0, 1, 2])))


main()