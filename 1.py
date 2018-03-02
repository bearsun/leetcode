#simple mapping between num and rest of sum
# one pass
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nd = dict()
        for i in range(len(nums)):
            if nums[i] in nd.keys():
                return sorted([i, nd[nums[i]]])
            else:
                nd[target-nums[i]] = i