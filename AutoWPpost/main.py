from bs4 import BeautifulSoup
import requests
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc import Client, WordPressPost
import pickle
import os
#variables
wp = Client('http://WP-WEBSITE/xmlrpc.php', 'USER', 'PASS')
videoID = []
urls = []
names = []
def deletevariables():
    variablesfordelete = [videoID,urls,names]
    for i in variablesfordelete:
        del i[:]
def scrapprofile(profilelink):
    #VZEMA LINKOVETE I IMENATA OT YOUTUBE
    result = requests.get(profilelink)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    #SLAGA GI V LIST NAMES I URLS
    for h2_tag in soup.find_all('h3'):
        a = h2_tag.find('a')
        try:
            if 'href' and 'title' in a.attrs:
                urls.append(a.attrs['href'])
                names.append(a.attrs['title'])
        except:
            pass
        #SCRAPVA VIDEOID
    for i in urls:
        videoID.append(i[9:])
    print('profile link scrapped')
def scrapplaylist(listlink):
    sourceCode = requests.get(listlink).text
    soup = BeautifulSoup(sourceCode, 'html.parser')
    for link in soup.find_all("a", {"dir": "ltr"}):
        href = link.get('href')
        if href.startswith('/watch?'):
            names.append(link.string.strip())
            urls.append(href)

    for i in urls:
        videoID.append(i[9:20])
    print('Listlink scrapped')
def posting(name,videoID,categoria):
  downloadlink = 'http://svali.ga:8080/out/' + str(videoID)
  post = WordPressPost()
  post.title = ''+str(name)+''
  post.content = '<p>'+str(name)+'<p><iframe width="560" height="315" align="center" src="https://www.youtube.com/embed/'+ str(videoID) +'"></iframe></p><p><a href="'+downloadlink+'"><img src="http://svali.ga/wp-content/uploads/2020/04/toppng.com-images-buttons-download-red-download-button-5319x1572-1.png"></a></p>'
  post.mime_type = "text/html"
  post.post_status = 'publish'
  post.terms_names = {
    'post_tag': [''+str(name)+'', 'svali.ga' , 'download' , 'mp3' , 'svali'] ,
    'category': [''+categoria+'']
  }
  print('POSTVA - '+name)
  wp.call(NewPost(post))
def post(kategoria):
    if os.path.exists("db.p"):
        with open("db.p","rb") as db:
            postsfromwp=pickle.load(db)
    else:
        postsfromwp=[]
    celi=dict(zip(names,videoID))

    print(celi)
    print(postsfromwp)
    print('izvlecheni postove-'+ str(len(postsfromwp)))

    for key, value in celi.items():
        if str(key) == 'nan' or str(key) == '[Частен видеоклип]' or str(key) == '[Изтрит видеоклип]' or str(key) in postsfromwp :
            pass
        else:
            posting(name=(key), videoID=(value),categoria=kategoria)
            postsfromwp.append(key)
    with open("db.p", "wb") as db:
        pickle.dump(postsfromwp,db)
