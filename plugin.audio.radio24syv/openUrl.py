import urllib2

# Small file which is being reused a lot in this project

def Open_Url(url):
    req = urllib2.Request(url)  
    response = ''
    link = ''
    try: 
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
    except: pass
    if link != '':
        return link
    else:
        link = 'Opened'
        return link