# interesting phase mismatch
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        count = 0
        for i in range(k):
            temp1 = nums[i]
            nxt = (i + k) % n
            while 1:
                temp2 = nums[nxt]
                nums[nxt] = temp1
                count += 1
                temp1 = temp2
                if i == nxt:
                    break
                else:
                    nxt = (nxt + k) % n
            if count >= n:
                break