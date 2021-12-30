import requests
import os

username = ''#Your UZEM Username.
password = ''#Your UZEM Password.

session = requests.session()

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def getCookies():
    session.post('https://ue.beun.edu.tr:443/', verify=False)
    session.cookies.set('CookUserName', username)
    session.post('https://ue.beun.edu.tr:443/', verify=False, data= {'Password': password})

def readFile(fileName):
        fileObj = open(fileName, "r") #Opens the file in read mode.
        words = fileObj.read().splitlines() #Puts the file into an array.
        fileObj.close()
        return words

def parseUrl(url):
    return url[43:-78]

def parseUrls():
    ids= []
    for i in readFile('urls.txt'): #Reads the urls from txt.
        if i[0] == '#': #Comment check.
            continue
        else:
            ids.append(parseUrl(i)) #Adds the urls into an array.
    print(ids)
    return ids

def getVideoUrl(id):
    url= 'https://ue.beun.edu.tr/Video/ManageInteraction?id=' + id

    r = session.post(url, verify=False, data = {'id': id})
    print('Got the direct download of: ' + id)

    #I hate myself for doing this. Please fix this if you are reading.
    #Variations of some url types. Works for all of my 23 videos.
    if r.text[154] == '/':
        return r.text[154:-47]
    elif r.text[153] == '/':
        return r.text[153:-47]
    else:
        return r.text[155:-47]

def assembleDownloads(headlessUrl):
    return 'https://ue.beun.edu.tr'+ headlessUrl

def main():
    print('Getting the cookies.')
    getCookies()
    links = []
    for i in parseUrls():
        read = session.get(assembleDownloads(getVideoUrl(i)), verify=False) #"reads" the video from the server
        print('Starting the download.')
        w = open(i + '.mp4', 'wb') #Creates or opens the video
        x = 0
        loading ='|\\-/'
        clear()
        for chunk in read.iter_content(chunk_size=512): #Divides data into chunks for ram i guess i stole this from the internet
            if chunk:
                w.write(chunk)
            print('downloading '+  i + loading[x % 4])
            x+=1

main()
