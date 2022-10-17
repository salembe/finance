"""
 @Author: amigo
 @Email: 88315203@qq.com
 @wechat: amigo_adios
 @DateTime: 2022/10/14 17:51
"""


# url = http://rsj.sh.gov.cn/tshbx_17729/20220117/t0035_1405188.html

def get_retire_money(social_avg_salary, your_salary, years=15):
    # social_avg_salary = 10000
    salary = your_salary

    def get_month_rate(y):
        r = (salary / social_avg_salary) + 1
        return r

    # years = 15
    month_rate = get_month_rate(years)
    self_avg_salary = social_avg_salary * month_rate

    got = (social_avg_salary + self_avg_salary) / 2 * years * 0.01
    return got


print(get_retire_money(social_avg_salary=10000, your_salary=30000, years=30))
print(get_retire_money(social_avg_salary=10000, your_salary=10000, years=15))
print(get_retire_money(social_avg_salary=10000, your_salary=5000, years=15))
