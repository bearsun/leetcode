class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        singledog = dict()
        for e in nums:
            singledog[e] = singledog.get(e,0) + 1
        return list(singledog.keys())[list(singledog.values()).index(1)]
        
    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unisum = sum(list(set(nums)))
        nsum = sum(nums)
        return nsum - (nsum - unisum) * 2