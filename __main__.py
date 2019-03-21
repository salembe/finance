#!/usr/bin/env python
# encoding: utf-8

"""
@author: amigo
@contact: 88315203@qq.com
@phone: 15618318407
@software: PyCharm
@file: __main__.py
@time: 2018/9/22 下午4:13
"""

from finance import Finance


def main():
    # f = Finance()
    # print f.cal_month_cost(10000, 0.023, 12)
    # print f.cal_annual_interest_rate(10000, 12, 984)
    years = [2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009]
    rates = [5.537, 5.537, 4.9, 4.165, 5.6, 6.15, 6.55, 6.8, 7.05, 6.14, 6.14]
    rates = [x / 100.0 for x in rates]
    print len(years), len(rates)
    print Finance.cal_house_income(10000, 0.3, 20, year_rate=0.06, sellout_year=10, odds=2)

    print Finance.cal_increase([2, 1.1, 1, 0.5])


if __name__ == '__main__':
    main()
