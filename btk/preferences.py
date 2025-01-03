import bpy

from . import asset_browser, editor_tools, node_graph_tools, object_tools, view_switcher
from .. import __name__ as addon_name


class BTK_AddonPreferences(bpy.types.AddonPreferences):
    bl_idname = addon_name

    @staticmethod
    def toggle_register(enabled: bool, module):
        _ = module.register() if enabled else module.unregister()

    enable_view_switcher: bpy.props.BoolProperty(
        name="Enable View Switcher", default=True, update=lambda self, _: BTK_AddonPreferences.toggle_register(self.enable_view_switcher, view_switcher)
    )

    enable_editor_tools: bpy.props.BoolProperty(
        name="Enable Editor Tools", default=True, update=lambda self, _: BTK_AddonPreferences.toggle_register(self.enable_editor_tools, editor_tools)
    )

    enable_object_tools: bpy.props.BoolProperty(
        name="Enable Object Tools", default=True, update=lambda self, _: BTK_AddonPreferences.toggle_register(self.enable_object_tools, object_tools)
    )

    enable_node_graph_tools: bpy.props.BoolProperty(
        name="Enable Node Graph Tools", default=True, update=lambda self, _: BTK_AddonPreferences.toggle_register(self.enable_node_graph_tools, node_graph_tools)
    )

    enable_assets_browser: bpy.props.BoolProperty(
        name="Enable Asset Browser Shortcut", default=True, update=lambda self, _: BTK_AddonPreferences.toggle_register(self.enable_assets_browser, asset_browser)
    )

    def draw(self, context):
        layout = self.layout

        layout.prop(self, "enable_view_switcher")
        layout.prop(self, "enable_editor_tools")
        layout.prop(self, "enable_object_tools")
        layout.prop(self, "enable_node_graph_tools")
        layout.prop(self, "enable_assets_browser")
