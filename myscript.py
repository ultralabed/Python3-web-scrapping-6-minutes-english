import pandas
import requests
from bs4 import BeautifulSoup

idUrlList=[]
epDataList=[]
base_url="http://www.bbc.co.uk/learningenglish/english"
main_args_url="/features/6-minute-english"

r=requests.get(base_url+main_args_url)
c=r.content
soup=BeautifulSoup(c,"html.parser")
allEpsList=soup.find_all("li", {"class": "course-content-item"})

for item in allEpsList:
    epId=item.div['data-feature-item']
    idUrlList.append(epId)

# print(idUrlList)    
    
for idUrl in idUrlList:
    r=requests.get(base_url+idUrl)
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    #HEADING
    print(soup.find_all("h3", {"dir": "ltr"})[1].text) 
    #AUDIO LINK
    print(soup.find_all("div", {"class":"bbcle-download-linkparent-extension-mp3"})[0].a['href'])
    
    break