'''
Project:pj1 file:5-20-1
Create date: 1/15/17.6:39 PM
TITLE:台灣大樂透 當期號螞查詢

使用PYTHON3 及爬蟲方式 讀取中獎資料

Create date: 1/15/17.7:34 PM
Author:vliucc  vliucc@gmail.com
'''
import requests
from bs4 import  BeautifulSoup
url="http://www.taiwanlottery.com.tw/index_new.aspx"
html=requests.get(url)
soup=BeautifulSoup(html.text,'html.parser')
dataA=soup.select("#rightdown")
dataB=dataA[0].find_all('div',{'class':'contents_box02'})
dataC=dataB[2].find_all('div',{'class':'ball_tx'})
dataC1=dataB[2].find('div',{'class':'ball_red'})
print('************ 大樂透開獎**************')
print('日期:',dataB[2].text[1:22])
for i in range(6,12):
    print(dataC[i].text,end='  ')
print

print('特別號：',dataC1.text)