from bs4 import BeautifulSoup
from datetime import datetime

import requests
r = requests.get("http://www.startribune.com/")
soup = BeautifulSoup(r.text)
with open('myfirstscrap.text', 'w') as scrap_info:
	scrap_info.writelines("Date scrapped: "+str(datetime.now().strftime("%A, %d. %B %Y %I:%M%p")+'\n'))
	scrap_info.writelines('Title of website:' +soup.title.string)

# print(soup.title.string, file=scrap_info)


for il_date in soup.find_all('ul', {'class':"nav-utility-inner nav-utility-inner-center"}):
	for date in il_date.find_all('li'):
		with open('myfirstscrap.text', 'a') as scrap_info:
			scrap_info.write('Date from website: '+ date.text)