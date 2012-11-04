from flask import Flask
import requests, time, os
from bs4 import BeautifulSoup

app = Flask(__name__)
cache = {}  # Poor Mans Cache
use_cache = os.getenv('USECACHE', False)  # Dont use cache in dev mode


def bs4_parse(web_source):
    soup = BeautifulSoup(web_source)
    projects_link = soup.body.find(href="http://bit.ly/hh-projects")
    projects_link["href"] = "http://hurricanehackers.com/projects"
    linkslist_link = soup.body.find(href="http://bit.ly/hh-linklist")
    linkslist_link["href"] = "http://hurricanehackers.com/links"
    return soup.prettify()


def fetchDoc(docid):
    if docid in cache.keys():
        if time.time()-cache[docid][0] < 300:  # 5 mins
            return cache[docid][1]
    f = requests.get('https://docs.google.com/feeds/download/documents/export/Export', params={'id':docid, 'exportFormat':'html'})
    if f.status_code != 200:
        return "We're having issues right now. Please <a href=\"https://images.google.com/?q=pictures+of+bears\">bear</a> with us."
    if use_cache: cache[docid] = [time.time(), f.text]
    return bs4_parse(f.text)


@app.route('/')
def route_root():
    return fetchDoc('1SGcfQz13ce4FfB-QHKF3WLwxHoCRGBouuvZn-3aoX0k')


@app.route('/links')
def link_page():
    return fetchDoc('1xmKiUVy2vZbluQbtItbN8WMQXPiWCt7f8DVKJe6_w0c')


@app.route('/projects')
def project_page():
    return fetchDoc('1wdDo65UcBfdcUTvda5fwb4HOI7RjEvWq3KzZBV9ORcc')

if __name__ == '__main__':
    app.run(debug=True) #We deploy using gunicorn, so this is safe
