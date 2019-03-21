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
    def cal_house_income(cls, down_payment, floor, year, year_rate, sellout_year=5, odds=2):
        """

        :param down_payment: 首付
        :param floor: 首付几成
        :param year: 贷款年限
        :param year_rate: 贷款年利率
        :param sellout_year: 出售年限
        :param odds: 房价在sellout_year内翻几倍
        :return:年化投资回报率
        """

        month = 12 * year  # 总房贷期数
        house_price = down_payment / floor
        loan = house_price * (1 - floor)

        def get_month_cost():
            if isinstance(year_rate, (int, float)):
                month_rate = year_rate / 12.0
                return [Finance.cal_month_cost(loan, month_rate, month)] * 12 * year
            elif isinstance(year_rate, list):
                _year_rate = []
                if len(year_rate) < year:
                    _year_rate = [year_rate[-1] for _ in range(year - len(year_rate))]
                year_rate.extend(_year_rate)
                _month_cost = []
                for y in year_rate:
                    month_rate = y / 12.0
                    _month_cost.extend([Finance.cal_month_cost(loan, month_rate, month)] * 12)
                return _month_cost

        month_cost = get_month_cost()

        invest_year_rate = 0.0001
        while True:
            all_month_cost = []
            base = 1.0 + (invest_year_rate / 12.0)
            for i in range(sellout_year * 12):
                month_count = i + 1
                benefit_month = sellout_year * 12 - month_count
                month_annual_cost = month_cost[i] * pow(base, benefit_month)
                if month == i:
                    break
                all_month_cost.append(month_annual_cost)
            all_month_cost.reverse()  # 月还款收益
            annual_down_payment = down_payment * pow(1 + invest_year_rate, sellout_year)  # 首付收益
            annual_cost = annual_down_payment + sum(all_month_cost)  # 总收益=首付收益+月还款收益

            left_debt = float(loan / year) * (year - sellout_year) if year > sellout_year else 0

            if (annual_cost + left_debt * 1.01) - house_price * odds < 0:
                invest_year_rate += 0.0001
            else:
                break
        return invest_year_rate

    @classmethod
    def cal_increase(cls, data_list):
        """

        :param data_list:
        :return:
        """
        res = [0.0] * len(data_list)
        for i, data in enumerate(data_list):
            if i == len(data_list) - 1:
                break
            res[i] = float(data_list[i] - data_list[i + 1]) / float(data_list[i + 1])

        compound_rate = cls.cal_compound_rate(data_list[-1], data_list[0], len(data_list) - 1)
        return compound_rate, res
