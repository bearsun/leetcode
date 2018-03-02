# sort and reduce to 2sum, and then check for duplicated numbers
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        sol = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            # two sum
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] < target:
                    l+=1
                elif nums[l] + nums[r] > target:
                    r-=1
                else:
                    sol.append([nums[i], nums[l], nums[r]])
                    while l < r:
                        if nums[l] == nums[l+1]:
                            l+=1
                        elif nums[r] == nums[r-1]:
                            r-=1
                        else:
                            break
                    l+=1
                    r-=1
        return sol