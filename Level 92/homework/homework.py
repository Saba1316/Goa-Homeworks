# Leetcode: 128. Longest Consecutive Sequence

# class Solution:
#     def longestConsecutive(self, nums: list[int]) -> int:
#         s = set(nums)
#         ans = 0
#         # d = defaultdict(int)
#         for x in nums:
#             y = x
#             while y in s:
#                 s.remove(y)
#                 y += 1
#             d[x] = d[y] + y - x
#             ans = max(ans, d[x])
#         return ans