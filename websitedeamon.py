from flask import Flask
from bs4 import BeautifulSoup
import urllib

app = Flask(__name__)


def bs4_slice(web_source):
    soup = BeautifulSoup(web_source)
    soup.body.find(id="header").decompose()
    soup.body.find(id="footer").decompose()
    for i in soup.body("img"):
        i["src"] = "https://docs.google.com/document/" + i["src"]
    return soup.prettify()


@app.route('/')
def hello_world():
    webpage = urllib.urlopen("https://docs.google.com/document/pub?id=1SGcfQz13ce4FfB-QHKF3WLwxHoCRGBouuvZn-3aoX0k").read()
    webpage = bs4_slice(web_source=webpage)
    return webpage

if __name__ == '__main__':
    app.run(debug=True)
