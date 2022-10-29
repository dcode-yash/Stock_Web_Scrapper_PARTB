import scrapy
import pandas as pd
import sqlite3

conn = sqlite3.connect('stocksdata_2.db')
c = conn.cursor()
#c.execute('''CREATE TABLE data(company_name TEXT,BUYTriggerPrice REAL,BUYStopLoss REAL,BUYStockTarget1 REAL,BUYStockTarget2 REAL,SELLTriggerPrice REAL,SELLStopLoss REAL,SELLStockTarget1 REAL,SELLStockTarget2 REAL)''')


class QuotesSpider(scrapy.Spider):
    name = "stocks_1"

    start_urls = []

    data = pd.read_csv('EQUITY_L.csv')
    df = data.head(1826)
    codes = df['SYMBOL'].tolist()
    
    for code in codes:
        lis = 'https://www.stocklinedirect.com/stock-tips-%s.html' % code
        start_urls.append(lis)


    def parse(self, response):
        company_name = response.css('h1.font-weight-normal.text-secondary span::text').get()
        i = 1
        for item in response.css('div.col-6.col-md-6.col-lg-3.p-1.font-weight-bold'):
            if i == 1:
                BUYTriggerPrice = item.css('ul.list-group li.list-group-item.p-1.h4::text').get()
                i += 1
            elif i == 2:
                BUYStopLoss = item.css('ul.list-group li.list-group-item.p-1.h4::text').get()
                i += 1
            elif i == 3:
                BUYStockTarget1 = item.css('ul.list-group li.list-group-item.p-1.h4::text').get()
                i += 1
            elif i == 4:
                BUYStockTarget2 = item.css('ul.list-group li.list-group-item.p-1.h4::text').get()
                i += 1
            elif i == 5:
                SELLTriggerPrice = item.css('ul.list-group li.list-group-item.p-1.h4::text').get()
                i += 1
            elif i == 6:
                SELLStopLoss = item.css('ul.list-group li.list-group-item.p-1.h4::text').get()
                i += 1
            elif i == 7:
                SELLStockTarget1 = item.css('ul.list-group li.list-group-item.p-1.h4::text').get()
                i += 1
            else:
                SELLStockTarget2 = item.css('ul.list-group li.list-group-item.p-1.h4::text').get()
                i += 1
        #c.execute('''INSERT INTO data VALUES(?,?,?,?,?,?,?,?,?)''', (company_name,BUYTriggerPrice,BUYStopLoss,BUYStockTarget1,BUYStockTarget2,SELLTriggerPrice,SELLStopLoss,SELLStockTarget1,SELLStockTarget2))
        #conn.commit()
    
    c.execute('''SELECT * FROM data ''')
    results = c.fetchall()
    print(results)
    conn.close()
    