import requests
from bs4 import BeautifulSoup
import time

html = requests.get("https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001")
soup = BeautifulSoup(html.content, "html.parser")

issue_list = soup.select('.photo > a')
cnt = 1

print('['+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+' 기준 네이버 속보]\n')

for item in issue_list:
    detail_view_html = requests.get(item.attrs['href'])
    detail_view_soup = BeautifulSoup(detail_view_html.content, "html.parser")

    titles = detail_view_soup.select('#articleTitle')

    for title in titles :
        print(str(cnt) + " : " + title.get_text())
        cnt = cnt + 1
