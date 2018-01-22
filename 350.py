class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1, dict2 = dict(), dict()
        for i in nums1:
            dict1[i] = dict1.get(i,0) + 1
        for i in nums2:
            dict2[i] = dict2.get(i,0) + 1
        
        inter = []
        for key, value in dict1.items():
            if key in dict2.keys():
                inter.extend([key] * min(value, dict2[key]))
        return inter