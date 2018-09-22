#!/usr/bin/env python
# encoding: utf-8

"""
@author: amigo
@contact: 88315203@qq.com
@phone: 15618318407
@software: PyCharm
@file: cal_rate.py
@time: 2018/9/22 上午9:56
"""

"""
等额本息还款公式推导 设贷款总额为A，银行月利率为β，总期数为m（个月），月还款额设为X

X = A*B*pow(1+B,m) / (pow(1+B,m)-1)
"""


class CalRate(object):
    @classmethod
    def cal_X(cls, A, B, m):
        return A * B * pow(1 + B, m) / (pow(1 + B, m) - 1)

    @classmethod
    def cal_M(cls, A, m, X):
        b = 0.00000001
        step = 0.00000001
        while True:
            last_x = cls.cal_X(A, b, m)
            # print "last_x=", last_x
            if last_x - X > 0:
                break
            else:
                b += step
        return b * 12


def main():
    A = 250000
    B = 0.05537 / 12
    m = 20 * 12
    X = 1724.94684016
    print CalRate.cal_X(A, B, m)
    print CalRate.cal_M(A, m, X)
    print CalRate.cal_M(45000, 12, 4186.5)


if __name__ == '__main__':
    main()
