import requests
# BeautifulSoup將文字轉換成object
from bs4 import BeautifulSoup


def main():
    url = 'https://www.imdb.com/chart/top/'
    # requests 連接網站
    source_code = requests.get(url)
    html = source_code.text
    # features="html.parser"為系統希望我們加上去，才不會Error!!!
    soup = BeautifulSoup(html, features="html.parser")
    items = soup.find_all('td', {'class': 'titleColumn'})
    d = {}
    for item in items:
        title_ = item.a['title']
        print(item.a)
        name = title_.split('(')[0]
        if name in d:
            d[name] += 1
        else:
            d[name] = 1
    for key, value in sorted(d.items(), key=lambda s: s[1]):
        print(key, '->', value)









    # items = soup.find_all('td', {'class': 'ratingColumn imdbRating'})
    # # print(item.span.text)
    # d = {}
    # total = 0
    # count = 0
    # for item in items:
    #     count += 1
    #     total += float(item.strong.text)
    #     #
    # print(total / count)







    # items = soup.find_all('td', {'class': 'titleColumn'})
    # # print(item.span.text)
    # d = {}
    # for item in items:
    #     if item.span.text in d:
    #         d[item.span.text] += 1
    #     else:
    #         d[item.span.text] = 1
    # for key, value in sorted(d.items(), key=lambda s: s[1]):
    #     print(key, '->', value)







if __name__ == '__main__':
    main()