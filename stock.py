import baostock as bs
import pandas as pd
import datetime


def main():
    lg = bs.login()
    sh = "sh.000001"
    sz = 'sz.399001'
    metrics = "date,code,open,high,low,close,preclose,volume,amount,pctChg"
    start_date = '2014-01-01'
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
    result = pd.merge(sh_r, sz_r, on='date')
    result['amount_x'] = result['amount_x'].astype('float64')
    result['amount_y'] = result['amount_y'].astype('float64')
    result['sum_amount'] = result['amount_x'] + result['amount_y']
    result = result[result['sum_amount'] >= 10000 * 10000 * 10000]
    pd.set_option('display.max_rows', None)
    print(result.sort_values('date'))

    # 登出系统
    bs.logout()


if __name__ == '__main__':
    main()
