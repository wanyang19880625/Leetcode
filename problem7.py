# @Time    : 2017/7/23 17:29
# @Author  : wanyang
# @Mail    ：wanyangnumberone@gmail.com
# @Git     ：https://github.com/wanyang19880625
# @Question：https://leetcode.com/problems/reverse-integer/#/description
# @Answer  ：
import re


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reversenum = list(str(abs(x)))[::-1]
        matchstr = re.findall("[^!0][0-9]+", ("").join(reversenum))
        result = int(("").join(list(matchstr)))
        if result > 2 ** 31 or result < -2 ** 31:
            return 0
        if x < 0:
            return 0 - result
        elif x > 0:
            return result
        elif x == 0:
            return 0
