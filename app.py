from flask import Flask
from bs4 import BeautifulSoup
import urllib, time

app = Flask(__name__)
cache = None
cache_time = 0

def bs4_slice(web_source):
    soup = BeautifulSoup(web_source)
    soup.body.find(id="header").decompose()
    soup.body.find(id="footer").decompose()
    for i in soup.body("img"):
        i["src"] = "https://docs.google.com/document/" + i["src"]
    return soup.prettify()

def render_doc():
    try:
        webpage = urllib.urlopen("https://docs.google.com/document/pub?id=1SGcfQz13ce4FfB-QHKF3WLwxHoCRGBouuvZn-3aoX0k").read()
        return bs4_slice(webpage)
    except:
        return "We're having some technical difficulties. Please check back soon!"

@app.route('/')
def route_root():
    global cache, cache_time
    if time.time()-cache_time > 300:
        cache = render_doc()
        cache_time = time.time()
        return cache

if __name__ == '__main__':
    app.run()
