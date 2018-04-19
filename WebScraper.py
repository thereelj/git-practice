from urllib.request import urlopen as URLLibRequest
from bs4 import BeautifulSoup

MovieList = 'https://www.sureseats.com/movies'

# opening connection to the page
URLClient = URLLibRequest(MovieList)
page_html = URLClient.read()
URLClient.close()

# html parser
page_BS4 = BeautifulSoup(page_html, "html.parser")# git-practice
