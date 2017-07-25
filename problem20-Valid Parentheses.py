# @Time    : 2017/7/25 20:37
# @Author  : wanyang
# @Mail    ：wanyangnumberone@gmail.com
# @Git     ：https://github.com/wanyang19880625
# @Question：https://leetcode.com/problems/valid-parentheses/#/description
# @Answer  ：

import re
class Solution(object):
    def isValid(self, s):
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif char == ")" and stack and stack[-1] == "(":
                stack.pop()
            elif char == "}" and stack and stack[-1] == "{":
                stack.pop()
            elif char == "]" and stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
        return stack == []