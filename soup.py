import requests
from bs4 import BeautifulSoup
url="https://bangla.bdnews24.com/"
response=requests.get(url)
soup =BeautifulSoup(response.content, "html.parser")
print(soup.content)
get_info =print(soup.find('h5', {'class':'default'}))
print(get_info)



# import requests
# r=requests.get('https://www.facebook.com/')
# print(r.text)
# print(r.status_code)
