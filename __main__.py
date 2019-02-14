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
    f = Finance()
    print f.cal_month_cost(10000, 0.023, 12)


if __name__ == '__main__':
    main()
