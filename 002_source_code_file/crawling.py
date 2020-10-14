import requests
from bs4 import BeautifulSoup

# 웹 페이지를 가져온 뒤 BeautifulSoup 객체로 만듦
url = "http://www.weather.go.kr/weather/observation/currentweather.jsp"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table", {"class" : "table_develop3"})
data = []

for tr in table.find_all("tr"):
  tds = list(tr.find_all("td"))
  for td in tds:
    if td.find('a'):
      point = td.find('a').text
      temperature = tds[5].text
      humidity = tds[9].text
      data.append([point, temperature, humidity])

with open('weather.csv', 'w') as file:
  file.write('point,temperature,humidity\n')
  for i in data:
    file.write('{0},{1},{2}\n'.format(i[0], i[1], i[2]))


# %matplotlib inline
import pandas as pd                # 데이터를 저장하고 처리하는 패키지
import matplotlib as mpl           # 그래프를 그리는 패키지
import matplotlib.pyplot as plt    # 그래프를 그리는 패키지

# csv 파일을 읽어서 DataFrame 객체로 만듦. 인덱스 컬럼은 point로 설정
df = pd.read_csv('weather.csv', index_col='point', encoding='utf8')

city_df = df.loc[['서울', '인천', '대전', '대구', '광주', '부산', '울산']]

# macOS 한글 폰트 설정
mpl.rc('font', family='AppleGothic')

# 차트 종류, 제목, 차트 크기, 범례, 폰트 크기 설정
ax = city_df.plot(kind='bar', title='날씨', figsize=(12, 4), legend=True, fontsize=12)
ax.set_xlabel('도시', fontsize=12)          # x축 정보 표시
ax.set_ylabel('기온/습도', fontsize=12)     # y축 정보 표시
ax.legend(['기온', '습도'], fontsize=12)    # 범례 지정
plt.show()