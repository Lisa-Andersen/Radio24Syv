import json
import openUrl

#
# A class for creating a list of categories
#

#Class defining a category

class Category:
    def __init__(self, name, programIds):
        self.name = name
        self.programIds = programIds

def Get_Categories():
    categories = []
    open_url = openUrl.Open_Url("http://api.radio24syv.dk/v2/topics")
    jsonData = json.loads(open_url)
    for category in jsonData:
        programs = []
        for program in category["albums"]:
            programs.append(program)
        categories.append(Category(category["name"].encode("utf-8"), programs))
    return categories
