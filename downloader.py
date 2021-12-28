import requests
import urllib.request
import json
import urllib.request
import time

#You need to go to your class and right click copy the videos link. Copying the url from the top of the video works too.
#There will still be failed downloads i couldn't get the request to json to work properly so i did whatever i can to make it work most of the time.

#You need to get these forum your browsers cookiejar. (Developer console -> applicaiton tab -> cookies (For Chrome))
verification = ''
sessionid = ''
auth = ''

#Copied form stack overflow .d
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words

def parseUrl(url):
    return url[43:-78]

def parseUrls():
    ids= []
    for i in readFile('urls.txt'):
        ids.append(parseUrl(i))
    print(ids)
    return ids

#Uses requests and cookies to get videos. Very rude of them to make it this hard. Very secure tho.
def getVideoUrl(id):
    url= 'https://ue.beun.edu.tr/Video/ManageInteraction?id=' + id

    r = requests.post(url, verify=False, data = {'id': id}, cookies = {'__RequestVerificationToken':verification, 'ASP.NET_SessionId':sessionid, '.ASPXAUTH':auth})
    if r.text[154] == "/": #Whatever i can to make it work most of the time.
        return r.text[154:-47]
    else:
        return r.text[155:-47]

def assembleDownloads(headlessUrl):
    return 'https://ue.beun.edu.tr'+ headlessUrl

#Gets the parsed urls and Downloads them.
def main():
    links = []
    for i in parseUrls():
        read = requests.get(assembleDownloads(getVideoUrl(i)), verify=False, cookies={'__RequestVerificationToken':verification, 'ASP.NET_SessionId':sessionid, '.ASPXAUTH':auth})
        w = open(i + '.mp4', 'wb')
        time.sleep(1)
        for chunk in read.iter_content(chunk_size=4096):
            if chunk:
                w.write(chunk)
            print(i + ' downloaded successfully!!!')

main()
