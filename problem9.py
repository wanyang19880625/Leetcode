# @Time    : 2017/7/24 20:46
# @Author  : wanyang
# @Mail    ：wanyangnumberone@gmail.com
# @Git     ：https://github.com/wanyang19880625
# @Question：https://leetcode.com/problems/palindrome-number/#/description
# @Answer  ：

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x_str = str(x)
        reverse_x_str =  ("").join(list(str(x))[::-1])
        if x_str == reverse_x_str:
            return True
        else:
            return False