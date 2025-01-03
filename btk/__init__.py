import bpy

from .preferences import BTK_AddonPreferences

from . import editor_tools, view_switcher, asset_browser, object_tools, node_graph_tools
from .. import __name__ as addon_name


def register():
    bpy.utils.register_class(BTK_AddonPreferences)

    pref: BTK_AddonPreferences = bpy.context.preferences.addons[addon_name].preferences

    if pref.enable_editor_tools:
        editor_tools.register()
    if pref.enable_view_switcher:
        view_switcher.register()
    if pref.enable_assets_browser:
        asset_browser.register()
    if pref.enable_object_tools:
        object_tools.register()
    if pref.enable_node_graph_tools:
        node_graph_tools.register()


def unregister():
    pref: BTK_AddonPreferences = bpy.context.preferences.addons[addon_name].preferences

    if pref.enable_node_graph_tools:
        node_graph_tools.unregister()
    if pref.enable_object_tools:
        object_tools.unregister()
    if pref.enable_assets_browser:
        asset_browser.unregister()
    if pref.enable_view_switcher:
        view_switcher.unregister()
    if pref.enable_editor_tools:
        editor_tools.unregister()

    bpy.utils.unregister_class(BTK_AddonPreferences)