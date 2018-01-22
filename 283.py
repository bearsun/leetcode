class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        n0 = 0
        while i < (len(nums)-n0):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                n0+=1
            else:
                i+=1