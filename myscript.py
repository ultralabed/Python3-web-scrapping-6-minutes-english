import pandas
import requests
from bs4 import BeautifulSoup

idUrlListCsv=[]
idUrlList=[]
epDataList=[]
base_url="http://www.bbc.co.uk/learningenglish/english"
main_args_url="/features/6-minute-english/"

r=requests.get(base_url+main_args_url)
c=r.content
soup=BeautifulSoup(c,"html.parser")
allEpsList=soup.find_all("li", {"class": "course-content-item"})

for item in allEpsList:
    epId=item.div['data-feature-item'].replace('/features/6-minute-english/','')
    epDate=item.div.nextSibling.nextSibling.nextSibling.nextSibling.h3.text.replace("\n","").replace("  ","").replace("				","").replace("	","").replace("  ","")
    idUrlListCsv.append({ 'id': epId, 'date': epDate })
    idUrlList.append(epId)

df=pandas.DataFrame(idUrlListCsv)
df.to_csv('IdList.csv')
    
for idUrl in idUrlList:
    r=requests.get(base_url+main_args_url+idUrl)
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    d={}

    #ID
    d["id"] = idUrl
    #HEADING
    d["heading"] = soup.find_all("h3", {"dir": "ltr"})[1].text
    #AUDIO LINK
    d["audio"] = soup.find_all("div", {"class":"bbcle-download-linkparent-extension-mp3"})[0].a['href']
    #TIME
    d["time"] = soup.find_all("div", {"class": "details"})[0].text.replace("\n","").replace("  ","").replace("				","")
    #Summary
    d["summary"] = soup.find_all("div", {"class": "widget-richtext"})[0].p.text
    # Question Title
    d["questionTitle"] = soup.find_all("div", {"class": "widget-richtext"})[0].h3.text
    # Vocabulary
    d["vocabularyTitle"] = 'Vocabulary'
    #Transcript 
    d["transcriptTitle"] = 'Transcript'
    
    #Get details
    detailContent=soup.find_all("div", {"class": "text"})[1]

    qList=[]
    vList=[]
    tList=[]
    i=0
    for child in detailContent.children:
        try:
            tag_name = child.name
        except AttributeError:
            tag_name = ""
        if tag_name == "h3":
            i=i+1
        if tag_name == "p":
            if i == 1:
                qList.append(child)
            elif i == 2:
                vList.append(child)
            elif i == 3:
                tList.append(child)
    #Question Detail
    d["questionDetail"] = qList
    #Vocabulary Detail
    d["vocabularyDetail"] = vList
    #Transcript Detail
    d["transcriptDetail"] = tList
    
    df=pandas.DataFrame([d,])
    with open('data.csv', 'a') as f:
        df.to_csv(f, header=False)
