# @Time    : 2017/7/23 16:44
# @Author  : wanyang
# @Mail    ：wanyangnumberone@gmail.com
# @Git     ：https://github.com/wanyang19880625
# @Question：https://leetcode.com/problems/two-sum/#/description
# @Answer  ：

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list = [(i,j) for i in range(0,len(nums)) for j in range(i+1,len(nums)) if nums[i]+nums[j] == target]
        return list[0]
