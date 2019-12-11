# -*- coding:utf-8 -*-
# ============================================
# Author: 郝天飞/Talen Hao (talenhao@gmail.com)
# Created at 2019-12-11 12:38 AM
# ============================================


class Solution:
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        row = len(matrix)
        if row == 0:
            return []
        col = len(matrix[0])
        order_list = []
        # 启点
        x, y = 0, 0
        to_east = 1
        to_south = 0
        to_west = 0
        to_north = 0
        min_row = 0
        max_row = row - 1
        min_col = 0
        max_col = col - 1
        has_matrix = row * col
        while has_matrix:
            # 判断是否在边界内 1. 添加到列表
            print("begin======={}===========================".format(has_matrix))
            print(min_row, max_row, min_col, max_col)
            print("x:{} y:{} ".format(x, y))
            if min_row <= x <= max_row and min_col <= y <= max_col:
                order_list.append(matrix[x][y])
                has_matrix -= 1
                print(order_list)
                if to_east:
                    y += 1
                    continue
                elif to_south:
                    x += 1
                    continue
                elif to_west:
                    y -= 1
                    continue
                elif to_north:
                    x -= 1
                    continue
            # 越界处理 1. 转向；2. 重修边界
            elif min_col <= max_col and min_row <= max_row:
                # print("other: {} {} {} {}".format(min_row, max_row, min_col, max_col))
                if to_east:
                    to_east = 0
                    to_south = 1
                    y -= 1
                    x += 1
                    min_row += 1
                elif to_south:
                    to_south = 0
                    to_west = 1
                    x -= 1
                    y -= 1
                    max_col -= 1
                elif to_west:
                    to_west = 0
                    to_north = 1
                    x -= 1
                    y += 1
                    max_row -= 1
                elif to_north:
                    to_north = 0
                    to_east = 1
                    x += 1
                    y += 1
                    min_col += 1
        return order_list


if __name__ == '__main__':
    nums = ([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ],)
    Solution_instance = Solution()
    for num in nums:
        print(Solution_instance.spiralOrder(num))

"""
螺旋矩阵
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
示例 1:
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:
输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
