# -*- coding:utf-8 -*-
# ============================================
# Author: 郝天飞/Talen Hao (talenhao@gmail.com)
# Created at 2019-12-10 11:15 AM
# ============================================
"""
加一

给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。


"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        1. 将整数列表转换成一个整数
        2. 整数+1
        3. 将整数各位数依次加入数组列表
        """
        plus_digits = [int(x) for x in str(int("".join(map(str, digits))) + 1)]
        return plus_digits


if __name__ == '__main__':
    nums1 = [1, 2, 3]
    nums2 = [4, 3, 2, 1]
    nums3 = [9]
    nums4 = [9, 9]
    Solution_instance = Solution()
    print(Solution_instance.plusOne(nums1))
    print(Solution_instance.plusOne(nums2))
    print(Solution_instance.plusOne(nums3))
    print(Solution_instance.plusOne(nums4))


