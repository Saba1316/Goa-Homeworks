# Leetcode: 217. Contains Duplicate

class Solution:
  def containsDuplicate(self, nums: list[int]) -> bool:
    return len(nums) != len(set(nums))