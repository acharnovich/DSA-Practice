# Given an array of numbers sorted in ascending order and a target sum, find a pair in the array whose sum is equal to the given target. 
# If no such pair exists return [-1, -1].
class Solution:
    def search(self, arr, target_sum):
        left = 0
        right = len(arr) - 1
        while(left < right):
            sum = arr[left] + arr[right]
            if sum == target_sum:
                return [left], [right]
            if target_sum > sum:
                left += 1
            else:
             right -= 1
        return [-1, -1]
    # a more optimized version using a hash map for O(n) complexity
    def optimizedSearch(self, nums, target_sum):
       prevMap = {}
       for i, n in enumerate(nums):
          diff = target_sum - n
          # finds the first index using map, then uses i as the other since it is index of n
          if diff in prevMap:
             return [prevMap[diff], i]
          prevMap[n] = i

def main():
  sol = Solution()
 # print(sol.search([1, 2, 3, 4, 6], 6))
 # print(sol.search([2, 5, 9, 11], 11)) 
  print(sol.optimizedSearch([1, 2, 3, 4, 6], 6))
  print(sol.optimizedSearch([2, 5, 9, 11], 11)) 

main()