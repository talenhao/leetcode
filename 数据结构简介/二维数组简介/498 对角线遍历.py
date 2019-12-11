# -*- coding:utf-8 -*-
# ============================================
# Author: 郝天飞/Talen Hao (talenhao@gmail.com)
# Created at 2019-12-10 2:28 PM
# ============================================
"""
给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。



示例:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

输出:  [1,2,4,7,5,3,6,8,9]

解释:



说明:

    给定矩阵中的元素总数不会超过 100000 。


"""
"""
行，列，斜线
遍历每一条斜线
奇偶正向反向
斜线启点终点
"""


class Solution(object):
    def findDiagonalOrder(self, matrix: "List[List[int]]") -> "List[int]":
        order_list = []
        row = len(matrix)
        if row == 0:
            return []
        col = len(matrix[0])
        line_num = row + col - 1
        # 遍历每条线
        x = 0
        y = 0
        reverse = 0
        for line in range(line_num):
            # print("line: {}================".format(line))
            # 奇偶定方向
            # if line % 2 == 0:
            #     reverse = 0
            #     print("reverse: {}, xy: {}, {}".format(reverse, x, y))
            # 启终点
            while reverse:
                # 反向下
                if x < row and y >= 0:
                    # print("向下:{} xy: {}, {}".format(reverse, x, y))
                    order_list.append(matrix[x][y])
                    x += 1
                    y -= 1
                elif x < row and y < 0:
                    # print("向下 y<0:{}, {}".format(x, y))
                    y += 1
                    reverse = 0
                    # print("向下反向:reverse: {}, xy: {}, {}".format(reverse, x, y))
                elif x >= row and y >= 0:
                    # print("向下 x>row:{}, {}".format(x, y))
                    x -= 1
                    y += 2
                    reverse = 0
                    # print("向下反向:reverse: {}, xy: {}, {}".format(reverse, x, y))
                elif x >= row and y < 0:
                    x -= 1
                    y += 2
                    reverse = 0
            while not reverse:
                # 正向上
                if x >= 0 and y < col:
                    # print("向上:{}, xy: {}, {}".format(reverse, x, y))
                    order_list.append(matrix[x][y])
                    x -= 1
                    y += 1
                    # print("next向上:{}, xy:{}, {}, list: {}".format(reverse, x, y, order_list))
                elif x < 0 and y < col:
                    x += 1
                    reverse = 1
                    # print("向上反向:reverse: {}, xy: {}, {}".format(reverse, x, y))
                elif x >= 0 and y >= col:
                    y -= 1
                    x += 2
                    reverse = 1
                    # print("向上反向:reverse: {}, xy: {}, {}".format(reverse, x, y))
                elif x < 0 and y >= col:
                    x += 2
                    y -= 1
                    reverse = 1
        return order_list


if __name__ == '__main__':
    nums = ([
             [1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]
    ], [])
    Solution_instance = Solution()
    for num in nums:
        print(Solution_instance.findDiagonalOrder(num))
