#!/usr/bin/python
import urllib                                
def main():
    sock = urllib.urlopen("")
    htmlSource = sock.read()
    sock.close()
    idx1=htmlSource.find("<body>")
    idx2=htmlSource.find("</body>",idx1)
    thebitwewant = htmlSource[idx1:idx2].strip()
    print "Content-type: text/html"
    print
    print thebitwewant
if __name__ == "__main__":
    main()
