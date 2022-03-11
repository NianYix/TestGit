import requests
url = 'https://www.cnblogs.com/zijiyanxi/p/5231159.html'
r = requests.get(url)
print(r.headers)