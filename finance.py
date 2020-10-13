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

import pandas as pd

pd.set_option('display.max_rows', 500)  # 打印最大行数
pd.set_option('display.max_columns', 500)  # 打印最大列数


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
            print("输入错误")
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

        house_price = down_payment / floor  # 房子总价
        loan = house_price * (1 - floor)  # 房屋总贷款额度

        def RepaymentCalculator(Loans, Year, YearRate, Type="等额本息"):
            """
            Loans:贷款总额
            Year: 贷款期限，单位年
            YearRate:贷款年利率
            Type: 还款方式，"等额本金"or"等额本息"
            """
            Month = Year * 12  # 贷款总月数
            MonthRate = YearRate / 12
            if (Type == "等额本息"):
                # 先求每个月固定还款额
                FixedPayment = (Loans * MonthRate * ((1 + MonthRate) ** Month)) / (
                        (1 + MonthRate) ** Month - 1)
            elif (Type == "等额本金"):
                FixedPayment = Loans / Month

            repayMonthIndex = []
            repayMonthPrincipal = []
            repayMonthInterest = []
            unpayPrincipal = []
            # 剩余本金
            UnpaidPrincipal = Loans
            if (Type == "等额本息"):
                for i in range(Month):
                    # 本月代还本金
                    unpayPrincipal.append(UnpaidPrincipal)
                    repayMonthIndex.append(i + 1)
                    # 先计算当月利息
                    thisMonthInterest = UnpaidPrincipal * MonthRate
                    repayMonthInterest.append(thisMonthInterest)
                    # 再计算当月本金
                    thisMonthPrincipal = FixedPayment - thisMonthInterest
                    repayMonthPrincipal.append(thisMonthPrincipal)
                    # 最后更新代还本金
                    UnpaidPrincipal = UnpaidPrincipal - thisMonthPrincipal
            elif (Type == "等额本金"):
                for i in range(Month):
                    # 本月代还本金
                    unpayPrincipal.append(UnpaidPrincipal)
                    repayMonthIndex.append(i + 1)
                    # 先计算当月利息
                    thisMonthInterest = UnpaidPrincipal * MonthRate
                    repayMonthInterest.append(thisMonthInterest)
                    # 再计算当月本金,等额本金不变哦
                    thisMonthPrincipal = FixedPayment
                    repayMonthPrincipal.append(thisMonthPrincipal)
                    # 最后更新代还本金
                    UnpaidPrincipal = UnpaidPrincipal - thisMonthPrincipal
            # 生成dataframe
            res = pd.DataFrame({
                "还款期数": repayMonthIndex,
                "未还本金": unpayPrincipal,
                "还款本金": repayMonthPrincipal,
                "还款利息": repayMonthInterest
            })
            res["还款总额"] = res["还款本金"] + res["还款利息"]
            # 调整小数位数
            res = res.round(2)
            return res

        df = RepaymentCalculator(Loans=loan, Year=year, YearRate=year_rate, Type="等额本息")
        month_cost = float(df.head()['还款总额'].iloc[0])  # 月供

        print('月供：', month_cost)

        invest_year_rate = 0.0001

        while True:
            all_month_cost = []
            base = 1.0 + invest_year_rate
            for i in range(sellout_year * 12):
                month_count = i + 1
                benefit_year = (sellout_year * 12 - month_count) / 12.0
                month_annual_cost = month_cost * pow(base, benefit_year)
                all_month_cost.append(month_annual_cost)
            all_month_cost.reverse()  # 月贷款+投资收益率

            annual_down_payment = down_payment * pow(base, sellout_year)  # 首付收益
            annual_cost = annual_down_payment + sum(all_month_cost)  # 总收益=首付收益+月还款收益

            left_debt = float(df['未还本金'][sellout_year * 12])

            if (annual_cost + left_debt) - house_price * odds <= 0:
                invest_year_rate += 0.0001
            else:
                print("已支付本金：", annual_cost)
                print("剩余本金：", float(df['未还本金'][sellout_year * 12]))
                print("房屋总价：", house_price * odds)
                print("支出：", annual_cost + left_debt)
                print("收入：", house_price * odds)
                # print(df.head())
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
