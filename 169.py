class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hist = dict()
        n = len(nums)//2
        for no in nums:
            hist[no] = hist.get(no,0) + 1
            if hist[no] > n:
                return no