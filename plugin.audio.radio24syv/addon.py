import sys
import xbmcaddon
import xbmcgui
import xbmcplugin
import categoryClass
import openUrl
from urllib import urlencode
from urlparse import parse_qsl


_handle = int(sys.argv[1])
_url = sys.argv[0]

ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.audio.radio24syv/')
addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo("name")
DEFAULT_ICON = ADDON_PATH + "icon.png"


################################### creating the menus ###############################################

def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.
    """
    return '{0}?{1}'.format(_url, urlencode(kwargs))

#Listing categories for xbmc creates the main menu
def mainMenu():
    categories = categoryClass.Get_Categories()
    for category in categories:
        list_item = xbmcgui.ListItem(label=category.name)
        list_item.setArt({'thumb': DEFAULT_ICON, 'icon': DEFAULT_ICON,'fanart': DEFAULT_ICON})
        list_item.setInfo('video', {'title': category.name, 'genre': category.name, 'mediatype': 'audio'})

        # For callbacks e.g plugin://plugin.audio.radio24syv/?action=programs&programs=<programIds>
        url = get_url(action='category', programs=category.name)
        is_folder = True
        # Add our item to the listing as a 3-element tuple.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    xbmcplugin.endOfDirectory(_handle)

################################### running the process ####################################

def router(paramstring):
    params = dict(parse_qsl(paramstring[1:]))
    if params:
        xbmcgui.Dialog().ok(addonname,  "No menu item")
    else:
        mainMenu()

if __name__ == '__main__':
    router(sys.argv[2][1:])