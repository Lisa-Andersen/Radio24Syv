import sys
import xbmcaddon
import xbmcgui
import xbmcplugin
import categoryClass
import openUrl
import programClass
from urllib import urlencode
from urlparse import parse_qsl


_handle = int(sys.argv[1])
_url = sys.argv[0]

ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.audio.radio24syv/')
addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo("name")
DEFAULT_ICON = ADDON_PATH + "icon.png"


################################### creating the menus ###############################################

# Listing categories for xbmc creates the main menu
def mainMenu():
    categories = categoryClass.Get_Categories()
    for category in categories:
        list_item = xbmcgui.ListItem(label=category.name)
        list_item.setArt({'thumb': DEFAULT_ICON, 'icon': DEFAULT_ICON,'fanart': DEFAULT_ICON})
        list_item.setInfo('audio', {'title': category.name, 'genre': category.name, 'mediatype': 'audio'})

        # For callbacks e.g plugin://plugin.audio.radio24syv/?action=programs&programs=Kultur
        #TODO: understand why this hack works!
        url = sys.argv[0] + "?aaction=category" + "&programs=" + category.name
        is_folder = True
        # Add our item to the listing as a 3-element tuple.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    xbmcplugin.endOfDirectory(_handle)
    
# Listing of programs under same category
def categoryMenu(categoryName):
    programs = programClass.Get_Programs(categoryName)
    for program in programs:
        list_item = xbmcgui.ListItem(label=program.name)
        list_item.setArt({'thumb': program.coverUrl, 'icon': program.coverUrl,'fanart': program.imageUrl})
        list_item.setInfo('audio', {'title': program.name, 'genre': program.category, "Plot": program.description, 'mediatype': 'audio'})

        # For callbacks e.g plugin://plugin.audio.radio24syv/?action=category&category=category.id
        url = sys.argv[0] + "?aaction=program" + "&program=" + str(program.id)
        is_folder = True
        # Add our item to the listing as a 3-element tuple.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    xbmcplugin.endOfDirectory(_handle)    


################################### running the process ####################################

def router(paramstring):
    params = dict(parse_qsl(paramstring[1:]))
    if params:
        if params['action'] == 'category':
            categoryMenu(params['programs'])
        else:
            xbmcgui.Dialog().ok(addonname,  "No menu item")
    else:
        mainMenu()

if __name__ == '__main__':
    router(sys.argv[2][1:])