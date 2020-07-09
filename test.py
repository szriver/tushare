import tushare as ts

# ts.set_token('346f7e043dfc7258ddf1bda702d5e9597dc502e2b9a580681ab891a0')
pro = ts.pro_api('346f7e043dfc7258ddf1bda702d5e9597dc502e2b9a580681ab891a0')

df = pro.trade_cal(exchange='', 
                   start_date='20200701', 
                   end_date='20200709', 
                   fields='exchange,cal_date,is_open,pretrade_date', 
                   is_open='0')

print(df)
