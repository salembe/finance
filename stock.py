import baostock as bs
import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    bs.login()
    sh = "sh.000001"
    sz = 'sz.399001'
    metrics = "date,code,open,high,low,close,preclose,volume,amount,pctChg"
    start_date = '2018-01-01'
    end_date = datetime.datetime.now().strftime('%Y-%m-%d')
    frequency = 'd'

    def get_result(t):
        rs = bs.query_history_k_data_plus(t,
                                          metrics,
                                          start_date=start_date, end_date=end_date, frequency=frequency)
        data_list = []
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        return pd.DataFrame(data_list, columns=rs.fields)

    sh_r = get_result(sh)
    sz_r = get_result(sz)
    print(sh_r)
    result = pd.merge(sh_r, sz_r, on='date')
    result['amount_x'] = (result['amount_x'].astype('float64') / (10000 * 10000)).astype(int)
    result['amount_y'] = (result['amount_y'].astype('float64') / (10000 * 10000)).astype(int)
    result['sum_amount'] = result['amount_x'] + result['amount_y']

    # 3000亿成交
    result = result[result['sum_amount'] >= 0]
    pd.set_option('display.max_rows', None)
    print(result.sort_values('date'))

    # 资金趋势
    sns.barplot("date", "sum_amount", palette="RdBu_r", data=result)
    plt.xticks(rotation=90)
    plt.show()

    # 登出系统
    bs.logout()


if __name__ == '__main__':
    main()
