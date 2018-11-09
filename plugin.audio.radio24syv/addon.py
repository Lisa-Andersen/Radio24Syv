import xbmcaddon
import xbmcgui

addon		= xbmcaddon.Addon()
addonname	= addon.getAddonInfo('name')

message = "Initial radio24syv addon"

xbmcgui.Dialog().ok(addonname, message)

