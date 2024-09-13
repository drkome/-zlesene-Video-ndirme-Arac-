import requests
from bs4 import BeautifulSoup



url = "https://www.izlesene.com/video/yasar-ipek-sevmek-yuzunden/10870852"
form = requests.get(url)
soup=BeautifulSoup(form.text,'html.parser')

for i in soup.find_all('meta',itemprop=True):
    if(i['itemprop']=="contentURL"):
        print(i['content'])
        video=i['content']
        form.close()
mp4=requests.get(video)
file=open("video.mp4","wb")
file.write(mp4.content)




