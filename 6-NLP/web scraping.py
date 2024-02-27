"""     Web Scrapping     """

from bs4 import BeautifulSoup
soup = BeautifulSoup(open("sample_doc.html"))
print(soup)
#It is going to show all the html contents extracted

soup.text
#it will only show text

soup.contents
#it is going to show all the html contents extracted

soup.find("address")
soup.find_all("address")
soup.find_all('q')
soup.find_all('b')









































