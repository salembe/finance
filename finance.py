#!/usr/bin/env python
# encoding: utf-8

"""
@author: amigo
@contact: 88315203@qq.com
@phone: 15618318407
@software: PyCharm
@file: finance.py
@time: 2018/9/22 下午4:05
"""

"""
等额本息还款公式推导 设贷款总额为A，银行月利率为β，总期数为m（个月），月还款额设为X

X = A*B*pow(1+B,m) / (pow(1+B,m)-1)
p = pow(float(_y) / _x, float(1) / _n) - 1
"""


class Finance(object):
    def __init__(self):
        pass

    @classmethod
    def cal_month_cost(cls, a, b, m):
        """
        计算每月还款金额(等额本息)
        :param a: 贷款总额
        :param b: 月利率
        :param m: 总期数
        :return: 月还款额
        """
        return a * b * pow(1 + b, m) / (pow(1 + b, m) - 1)

    @classmethod
    def cal_annual_interest_rate(cls, a, m, x):
        """
        计算年化利率
        :param a: 贷款总额
        :param m: 总期数
        :param x: 月还款额
        :return:
        """
        b = 0.00000001
        step = 0.00000001
        while True:
            last_x = cls.cal_month_cost(a, b, m)
            if last_x - x > 0:
                break
            else:
                b += step
        return b * 12

    @classmethod
    def cal_compound_rate(cls, _x, _y, _n):
        """
        计算复利利率
        :param _x:初始值
        :param _y:结果值
        :param _n:总年份
        :return:
        """
        return pow(float(_y) / _x, float(1) / _n) - 1
