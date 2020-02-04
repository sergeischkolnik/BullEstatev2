from bs4 import BeautifulSoup
import re
import os




def readHtml(fileName):

    with open(fileName) as inf:

        txt = inf.read()
        print(txt)
    return txt

def writeHtml(fileName,message):

    f = open(fileName, 'w')
    f.write(message)
    f.close()


def main():

    fileName="expert/index.html"
    txt=readHtml(fileName)
    txt=txt.replace("Not Awesome","Salvi")
    txt=txt.replace("We","Salvi")
    txt=txt.replace("Things","Salvi")

    writeHtml(fileName,txt)
if __name__ == '__main__':
    main()