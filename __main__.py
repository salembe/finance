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
    print('投资回报率:', Finance.cal_house_income(down_payment=1500000,
                                             floor=0.3,
                                             year=30,
                                             year_rate=0.05537,
                                             sellout_year=4,
                                             odds=1) * 100)


if __name__ == '__main__':
    main()
