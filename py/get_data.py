import tushare

def get_data(code):



    df = ts.get_realtime_quotes(str(code)) #Single stock symbol
    df[['code','name','price','bid','ask','volume','amount','time']]
    df.pop('name')
    print(df)





get_data()