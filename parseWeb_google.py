import urllib
import urllib2 
import mechanize 
import sys
import os
import time
from bs4 import BeautifulSoup
from urlparse import urlparse
import hashlib

def create_folder(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

def search_pic(search_terms):
    print "Total number of search tags:" + str(len(search_terms))

    for term in search_terms:
        create_folder(term)
        img_list = get_pic(term)
        if len(img_list) > 0:
            print "Total number of images:" + str(len(img_list))
            for img in img_list:
                s = time.clock()
                save_pic(img, term)
                print "time:" + str(time.clock() - s)
    print "done..."     

def get_pic (search):
    search = search.replace(" ","%20")
    try:
        browser = mechanize.Browser()
        browser.set_handle_robots(False)

        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:14.0) Gecko/20100101 Firefox/14.0.1', 'Referer': 'http://whateveritis.com'}
        url = "https://www.google.com/search?site=imghp&tbm=isch&source=hp&biw=1414&bih=709&q="+search+"&oq="+search

        request = urllib2.Request(url, None, header)
        
        htmltext = browser.open(request)
        img_urls = []
        formatted_images = []
        soup = BeautifulSoup(htmltext)
        results = soup.findAll("a")
        for r in results:
            try:
                if "imgres?imgurl" in r['href']:
                    img_urls.append(r['href'])
            except:
                a=0
        for im in img_urls:
            refer_url = urlparse(str(im))
            image_f = refer_url.query.split("&")[0].replace("imgurl=","")
            formatted_images.append(image_f)
        
        return  formatted_images

    except:
        return []

def save_pic(url, dir_name):
    hs = hashlib.sha224(url).hexdigest()
    file_extension = url.split(".")[-1]
    uri = ""
    dest = dir_name + "/" + uri+hs+"."+file_extension
    print (dest),
    try:
        urllib.urlretrieve(url,dest)
    except:
        print "save failed" 

def main():
    tagsfile = sys.argv[1]
    tags = map( str.strip, open(tagsfile).readlines())
    search_pic(tags)

if __name__ == '__main__':
    main()

