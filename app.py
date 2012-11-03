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
    projects_link = soup.body.find(href="http://bit.ly/hh-projects")
    projects_link["href"] = "http://hurricanehackers/projects"
    linkslist_link = soup.body.find(href="http://bit.ly/hh-linklist")
    linkslist_link["href"] = "http://hurricanehackers/links"
    return soup.prettify()


def render_doc(site):
    try:
        webpage = urllib.urlopen(site).read()
        return bs4_slice(webpage)
    except:
        return "We're having some technical difficulties. Please check back soon!"


@app.route('/')
def route_root():
    return render_doc("https://docs.google.com/document/pub?id=1SGcfQz13ce4FfB-QHKF3WLwxHoCRGBouuvZn-3aoX0k")


@app.route('/links')
def link_page():
    return render_doc("https://docs.google.com/document/pub?id=1xmKiUVy2vZbluQbtItbN8WMQXPiWCt7f8DVKJe6_w0c")


@app.route('/projects')
def project_page():
    return render_doc("https://docs.google.com/document/pub?id=1wdDo65UcBfdcUTvda5fwb4HOI7RjEvWq3KzZBV9ORcc")

if __name__ == '__main__':
    app.run(debug=True)
