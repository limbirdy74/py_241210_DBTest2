import requests
from bs4 import BeautifulSoup
import datetime


# 가장 최근 회차를 가져오기
url = f"https://dhlottery.co.kr/common.do?method=main"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
recentCount = soup.find("strong",{"id":"lottoDrwNo"}).text.strip() # 가장 로또 최근 회차
recentCount = int(recentCount)
print(recentCount)

lottoNumList = []
# for count in range(1, recentCount + 1): # 1~1149 회까지 반복
for count in range(1, 11): # test 1 ~ 10 회차
    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={count}"  # 로또 1회차 당첨번호 출력 url

    html = requests.get(url)
    # print(html.text)

    # 당첨번호
    soup = BeautifulSoup(html.text, "html.parser")
    lottoNumber = soup.find("div",{"class":"num win"}).find("p").text.strip().split("\n")
    # split("\n") -> ['10', '23', '29', '33', '37', '40']
    print(lottoNumber)

    # 보너스 번호
    bonusNumber = soup.find("div",{"class":"num bonus"}).find("p").text.strip()
    print(bonusNumber)

    # 로또 추첨일
    lottoDate = soup.find("p", {"class":"desc"}).text.strip()
    print(lottoDate) # (2002년 12월 07일 추첨)
    lottoDate = datetime.datetime.strptime(lottoDate, "(%Y년 %m월 %d일 추첨)")  # 문자열 날짜 -> 날짜 type 로 변환
    print(lottoDate) # 2002-12-07 00:00:00

    lottoData = {"date":lottoDate, "lottoNum":lottoNumber, "bonusNum":bonusNumber}
    # print(lottoData)

    lottoNumList.append(lottoData)

print(lottoNumList)

