from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, n in enumerate(nums):
            if n in nums_dict:
                return nums_dict[n], i
            nums_dict[target - n] = i
