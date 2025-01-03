import bpy

from .btk import editor_quick
from .btk import switch_view
from .btk import asset_browser
from .btk import object_quick
from .btk import node_graph


bl_info = {
    "name": "Bitsy Blender Toolkit",
    "description": "Utilities for Blender",
    "author": "Bitsy",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "location": "Editor > Bitsy",
    "support": "COMMUNITY",
    "category": "Utility",
}


class BtkPrefs(bpy.types.AddonPreferences):
    bl_idname = __name__

    @classmethod
    def toggle(cls, enabled: bool, module):
        _ = module.register() if enabled else module.unregister()

    enable_editor: bpy.props.BoolProperty(name="Enable Editor Tools", default=True, update=lambda self, _: BtkPrefs.toggle(self.enable_editor, editor_quick))
    enable_switch_view: bpy.props.BoolProperty(name="Enable View Switcher", default=True, update=lambda self, _: BtkPrefs.toggle(self.enable_editor, switch_view))
    enable_asset_browser: bpy.props.BoolProperty(name="Enable Quick Assets", default=True, update=lambda self, _: BtkPrefs.toggle(self.enable_editor, asset_browser))
    enable_object: bpy.props.BoolProperty(name="Enable Object Tools", default=True, update=lambda self, _: BtkPrefs.toggle(self.enable_editor, object_quick))
    enable_node: bpy.props.BoolProperty(name="Enable Node Graph", default=True, update=lambda self, _: BtkPrefs.toggle(self.enable_editor, node_graph))

    def draw(self, context):
        layout = self.layout

        layout.prop(self, "enable_editor")
        layout.prop(self, "enable_switch_view")
        layout.prop(self, "enable_asset_browser")
        layout.prop(self, "enable_object")
        layout.prop(self, "enable_node")


def register():
    bpy.utils.register_class(BtkPrefs)

    preferences: BtkPrefs = bpy.context.preferences.addons[__name__].preferences

    if preferences.enable_editor:
        editor_quick.register()
    if preferences.enable_switch_view:
        switch_view.register()
    if preferences.enable_asset_browser:
        asset_browser.register()
    if preferences.enable_object:
        object_quick.register()
    if preferences.enable_node:
        node_graph.register()


def unregister():
    preferences: BtkPrefs = bpy.context.preferences.addons[__name__].preferences

    if preferences.enable_node:
        node_graph.unregister()
    if preferences.enable_object:
        object_quick.unregister()
    if preferences.enable_asset_browser:
        asset_browser.unregister()
    if preferences.enable_switch_view:
        switch_view.unregister()
    if preferences.enable_editor:
        editor_quick.unregister()

    bpy.utils.unregister_class(BtkPrefs)
