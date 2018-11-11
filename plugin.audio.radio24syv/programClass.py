import json
import openUrl
import categoryClass
from warnings import catch_warnings

#
#Class defining and generating a program list

class Program:
    def __init__(self, name, description, id, coverUrl, imageUrl, category):
        self.name = name
        self.id = id
        self.imageUrl = imageUrl
        self.coverUrl = coverUrl
        self.description = description
        self.category = category
    
    
def Get_Programs(categoryName):
    programs = []
    programIds = categoryClass.Get_ProgramsFrom_Category(categoryName)
    for id in programIds:
        #If one fails the menu will create all others
        url = "http://api.radio24syv.dk/v2/programs/"+str(id)
        open_url = openUrl.Open_Url(url)
        jsonData = json.loads(open_url)
        if jsonData["active"]:
            #Setting data
            name = jsonData["name"]
            imageUrl = jsonData["metaInfo"]["image"]
            coverUrl =  jsonData["podcastCover"]["src"]
            description = jsonData["metaInfo"]["description"]
            programs.append(Program(name, description, id, coverUrl, imageUrl, categoryName))
    return programs