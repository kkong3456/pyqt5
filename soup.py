from bs4 import BeautifulSoup 
import requests

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup=BeautifulSoup(html_doc,'html.parser')

#print(soup.prettify())
# print(soup.p.string)

# print(soup.title.parent.name)

# print(soup.p['class'])
# print(soup.a)

# print(soup.find_all('a'))

# print(soup.find(id='link3'))

# for link in soup.find_all('a'):
#     print(link.get('href'))

# print(soup.get_text())

r=requests.get('https://google.com')
# print(r.text)
# print(r.content)

print(dir(r))
print(f'status_code is {r.status_code}')
print(f'r.headers is {r.headers["Content-Type"]}')
print(f'r.encoding is {r.encoding}')
print(f'r.ok is {r.ok}')