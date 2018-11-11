import json
import openUrl

# A class for defining and retrieving podcasts

class Podcast:
    def __init__(self, title, description, id, date, path, image):
        self.title = title
        self.description = description
        self.id = id
        self.date = date
        self.path = path
        self.image = image

def Get_Podcasts(id):
        podcasts = []
        open_url = openUrl.Open_Url("http://api.radio24syv.dk/v2/podcasts/program/"+str(id))
        print "http://api.radio24syv.dk/v2/podcasts/program/"+str(id)
        jsonData = json.loads(open_url)
        #retrieves 20 most recent podcast
        numberOfPodcasts = min(20,len(jsonData))
        for podcast in jsonData[:numberOfPodcasts]:
            title = podcast["title"]
            description = podcast["metaInfo"]["description"]
            image = podcast["metaInfo"]["image"]
            date = podcast["publishInfo"]["createdAt"]
            path ="https://arkiv.radio24syv.dk" + podcast["audioInfo"]["url"]
            podcasts.append(Podcast(title, description, id, str(date)[0:10], path, image))
        return podcasts
            
pod = Get_Podcasts(8879419)
print pod[0].path