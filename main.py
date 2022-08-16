from urllib import response
import requests
import os
import datetime


stock = "IBM"
api_key = "V19ALVB8TPXMQ9E3"
api_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&apikey={api_key}"

company_name = "IBM"


news_api_key = "c7959eefa89d4fe78fa34db49ee8f85c"
news_api_url = "https://newsapi.org/v2/everything"

r =  requests.get(api_url)
data = r.json()
data = data['Time Series (Daily)']

data_list = [values for (keys,values) in data.items()]


yesterday_data = data_list[0]
yesterday_closing = yesterday_data['4. close']
day_before_yesterday = data_list[1]
day_before_yesterday_closing = day_before_yesterday['4. close']
threshold = 5

print(yesterday_closing, day_before_yesterday_closing)
difference = abs(float(yesterday_closing) - float(day_before_yesterday_closing))
diff_percentage = difference/ float(yesterday_closing) * 100

print(diff_percentage)

if diff_percentage >= threshold:

    news_params = {
            "apiKey" : news_api_key,
            "qInTitle" : company_name
        }

    three_headlines = []
    response = requests.get(news_api_url, params=news_params)
    news = response.json()['articles']
# news = news[:3]

    for i in range(0,4):
        print(news[i]['title'])
        three_headlines.append(news[i]['title'])
    print(three_headlines)

    three_headlines.clear()

else:

    print(f"the percentage difference is not greather than {threshold} %")

