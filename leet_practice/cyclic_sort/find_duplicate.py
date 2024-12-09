class Solution:
  def sort(self, nums):
    i = 0
    while i < len(nums):
      j = nums[i] - 1  # Calculate the index where the current element should be placed.
      if nums[i] != nums[j]:  # Check if the current element is not in its correct position.
        nums[i], nums[j] = nums[j], nums[i]  # Swap the current element with the one at its correct position.
      else:
        i += 1  # If the current element is already in its correct position, move to the next element.
    for i in len(nums):
      if i == nums[i+1]:
        return i
    return nums