import math

class Solution:
  def findMinSubArray(self, s, arr):
    windowStart = 0
    windowSum = 0
    minLength = math.inf
    for windowEnd in range(0,len(arr)):
      windowSum += arr[windowEnd]
      while windowSum >= s:
        minLength = min(minLength, windowEnd - windowStart + 1)
        windowSum -= arr[windowStart]
        windowStart += 1
    if minLength == math.inf:
      return 0
    return minLength    
