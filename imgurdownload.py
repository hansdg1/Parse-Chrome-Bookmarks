import httplib
import sys
import urllib2,urllib
import os
import csv
import StringIO

if(len(sys.argv) > 1):
    imgurlinks = sys.argv[1]
else:
    imgurlinks="/home/h/hguthrie/imgurdl/imgurlinks_small.csv"

inputfile = csv.DictReader(open(imgurlinks))
deadlinks = open('deadlinks.csv','wb')
alivelinks = open('alivelinks.csv','wb')
alive = 0
dead = 0
for row in inputfile:
    response = urllib2.urlopen(urllib2.Request(row['url']))
    #print(response.getcode())
    if (row['url'] != response.geturl()):
        dead+=1
        deadlinks.write(row['url'] + ', ' + '"' + row['title'] + '"' + '\n')
    else:
        alive+=1
        alivelinks.write(row['url'] + ',' + '"' + row['title'] + '"' + '\n')
        path = "/home/h/hguthrie/imgurdl/images/" + row['title'] + row['url'][-4:]
        url = row['url']
        ext = row['url'][-4:]
        basepath = "/home/h/hguthrie/imgurdl/images/"
        filename = row['title'] + ext
        
        if (ext == '.gif'):
            path = basepath + 'gifs/'
            if not os.path.exists(path): 
                os.makedirs(path)
            urllib.urlretrieve(url,path + filename)
        #wget -p path row['url']
        elif (ext == '.jpg'):
            path = basepath + 'jpgs/'
            if not os.path.exists(path): 
                os.makedirs(path)
            urllib.urlretrieve(url,path + filename)
        elif (ext == '.png'):
            path = basepath + 'png/'
            if not os.path.exists(path): 
                os.makedirs(path)
            urllib.urlretrieve(url,path + filename)
 
 
print('Alive: ' + str(alive) + '\nDead: ' + str(dead))
