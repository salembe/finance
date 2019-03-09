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
        if m * x < a:
            print "输入错误"
            return -1
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

    @classmethod
    def cal_house_income(cls, down_payment, year, year_rate, sellout_year=5, invest_year_rate=0.12):
        """

        :param down_payment: 首付
        :param year: 贷款年限
        :param year_rate: 贷款年利率
        :param sellout_year: 出售年限
        :param invest_year_rate: 个人投资年收益率
        :return:
        """
        house_price = down_payment / 0.3
        month_rate = year_rate / 12.0
        month = 12 * year
        loan = house_price * 0.7
        month_cost = Finance.cal_month_cost(loan, month_rate, month)
        print 'month_cost=', month_cost

        all_month_cost = []

        base = 1.0 + (invest_year_rate / 12.0)
        for i in range(sellout_year * 12):
            month_count = i + 1
            benefit_month = sellout_year * 12 - month_count
            month_annual_cost = month_cost * pow(base, benefit_month)
            all_month_cost.append(month_annual_cost)
        all_month_cost.reverse()
        for i, cost in enumerate(all_month_cost):
            print i, cost
        annual_down_payment = down_payment * pow(1 + invest_year_rate, sellout_year)
        print annual_down_payment
        annual_cost = annual_down_payment + sum(all_month_cost)
        left_debt = (house_price * 0.7 / year) * (year - sellout_year)
        print 'left_debt=', left_debt

        print annual_cost + left_debt * 1.01, house_price * 2 - left_debt  # 违约金 1%
