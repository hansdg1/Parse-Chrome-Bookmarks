from bs4 import BeautifulSoup
import re
soup = BeautifulSoup(open("bookmarks_9_17_14.html"))


with open("parsed_imgur_links.csv","wb") as file:
    for link in soup.find_all('a',href=re.compile('imgur.com')):
        #print(link.get('href'),link.contents)
        #file.write(link.get('href') + ',' + link.contents[0] + '\n')
        print link.parent.contents.name
