class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxwater = 0
        i = 0
        j = len(height)-1
        while i < j:
            if height[i] >= height[j]:
                maxwater = max(maxwater, height[j]*(j-i))
                j -= 1
            else:
                maxwater = max(maxwater, height[i]*(j-i))
                i += 1
        return maxwater