#!/usr/bin/env python
# encoding: utf-8

"""
@author: amigo
@contact: 88315203@qq.com
@phone: 15618318407
@software: PyCharm
@file: cal_fina.py
@time: 2018/9/22 下午2:36
"""

"""

"""

s = "2,421,600	1,610,800	1,032,000	545,700	422,200".replace(",", "")

lls = s.split("\t")
lls = [float(x) for x in lls]
lls.reverse()


def cal_fina(_x, _y, _n):
    return pow(float(_y) / _x, float(1) / _n) - 1


rs = [0] * len(lls)
for i, item in enumerate(lls):
    if i == 0:
        rs[i] = cal_fina(lls[0], lls[-1], len(lls) - 1)
    else:
        rs[i] = cal_fina(lls[i - 1], lls[i], 1)

# print cal_fina(1, 10, 10)
rs.reverse()
print rs
