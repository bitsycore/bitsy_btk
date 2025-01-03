import bpy

from .preferences import BTK_AddonPreferences

from . import editor_quick, switch_view, asset_browser, object_quick, node_graph
from .. import __name__ as addon_name


def register():
    bpy.utils.register_class(BTK_AddonPreferences)

    preferences: BTK_AddonPreferences = bpy.context.preferences.addons[addon_name].preferences

    if preferences.enable_editor_tools:
        editor_quick.register()
    if preferences.enable_view_switcher:
        switch_view.register()
    if preferences.enable_assets_browser:
        asset_browser.register()
    if preferences.enable_object:
        object_quick.register()
    if preferences.enable_node:
        node_graph.register()


def unregister():
    preferences: BTK_AddonPreferences = bpy.context.preferences.addons[addon_name].preferences

    if preferences.enable_node:
        node_graph.unregister()
    if preferences.enable_object:
        object_quick.unregister()
    if preferences.enable_assets_browser:
        asset_browser.unregister()
    if preferences.enable_view_switcher:
        switch_view.unregister()
    if preferences.enable_editor_tools:
        editor_quick.unregister()

    bpy.utils.unregister_class(BTK_AddonPreferences)
