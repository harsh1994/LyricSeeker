from bs4 import BeautifulSoup
import requests
from urllib2 import urlopen
import re

print "Enter the song"

song_name = raw_input()
payload = {'search':song_name}
r = requests.get('http://www.lyricsmode.com/search.php', params = payload)

URL = r.url
soup = BeautifulSoup(urlopen(URL))
x=[]
for link in soup.find_all('a'):
     x.append(link.get('href'))

a=x[-1]



r1 = requests.get('http://www.lyricsmode.com'+a)

URL1 = r1.url
soup1 = BeautifulSoup(urlopen(URL1))


text = soup1.find_all("p", class_="ui-annotatable")
text = str(text)
text= text.replace("</p>]","")
text= text.replace('[<p class="ui-annotatable" id="lyrics_text">',"")
text= text.replace("<br/>","\n")

print re.sub("\n\s*\n*", "\n", text)
