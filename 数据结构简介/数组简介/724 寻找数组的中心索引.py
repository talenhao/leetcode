# -*- coding:utf-8 -*-
# ============================================
# Author: 郝天飞/Talen Hao (talenhao@gmail.com)
# Created at 2019-12-10 9:52 AM
# ============================================
"""
至少是其他数字两倍的最大数

在一个给定的数组nums中，总是存在一个最大元素 。

查找数组中的最大元素是否至少是数组中每个其他数字的两倍。

如果是，则返回最大元素的索引，否则返回-1。

示例 1:

输入: nums = [3, 6, 1, 0]
输出: 1
解释: 6是最大的整数, 对于数组中的其他整数,
6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.



示例 2:

输入: nums = [1, 2, 3, 4]
输出: -1
解释: 4没有超过3的两倍大, 所以我们返回 -1.



提示:

    nums 的长度范围在[1, 50].
    每个 nums[i] 的整数范围在 [0, 100].


"""
"""
# 小于2个数，返回-1
最大值有2个，返回-1
最大值小于一个值的2倍，返回-1
其它返回最大值index
"""


class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list_len = len(nums)
        if list_len >= 2:
            max_count = 0
            max_index = None
            list_max = max(nums)
            for key, value in enumerate(nums):
                if list_max == value:
                    max_count += 1
                    if max_count > 1:
                        return -1
                    else:
                        max_index = key
                elif list_max < value * 2:
                    return -1
            return max_index

        else:
            return 0


if __name__ == '__main__':
    nums1 = [3, 6, 1, 0]
    nums2 = [1, 2, 3, 4]
    nums3 = [1]
    Solution_instance = Solution()
    print(Solution_instance.dominantIndex(nums1))
    print(Solution_instance.dominantIndex(nums2))
    print(Solution_instance.dominantIndex(nums3))
