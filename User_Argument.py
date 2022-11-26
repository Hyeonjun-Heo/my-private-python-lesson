import requests

res = requests.get("http://nadocoding.tistory.com")

with open("nadocoding.html","w", encoding="utf8") as f:
    f.write(res.text)