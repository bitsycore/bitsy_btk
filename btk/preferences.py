import bpy
from .window_mode import WindowMode
from .. import __name__ as addon_name


class BTK_AddonPreferences(bpy.types.AddonPreferences):
    bl_idname = addon_name

    @staticmethod
    def on_toggle_register(enabled, mdoule_name):
        pass

    asset_browser_window_mode: bpy.props.EnumProperty(
        name="",
        description="Select the window mode",
        items=[(
            WindowMode.RENDER.name,
            WindowMode.RENDER.name,
            "Use Render Window (Custom Size)"
        ), (
            WindowMode.PREF.name,
            WindowMode.PREF.name,
            "Use Preference Window (Always on Top)"
        ), (
            WindowMode.NEW.name,
            WindowMode.NEW.name,
            "Basic new window"
        )],
        default=WindowMode.PREF.name
    )

    asset_browser_window_mode_x: bpy.props.IntProperty(
        name="Window Width",
        description="Select the window mode",
        default=800
    )

    asset_browser_window_mode_y: bpy.props.IntProperty(
        name="Window Height",
        description="Select the window mode",
        default=600
    )

    enable_view_switcher: bpy.props.BoolProperty(
        name="Enable View Switcher",
        default=True,
        update=lambda self, _: BTK_AddonPreferences.on_toggle_register(
            self, "view_switcher")
    )

    enable_editor_tools: bpy.props.BoolProperty(
        name="Enable Editor Tools",
        default=True,
        update=lambda self, _: BTK_AddonPreferences.on_toggle_register(
            self, "editor_tools")
    )

    enable_object_tools: bpy.props.BoolProperty(
        name="Enable Object Tools",
        default=True,
        update=lambda self, _: BTK_AddonPreferences.on_toggle_register(
            self, "object_tools")
    )

    enable_node_graph_tools: bpy.props.BoolProperty(
        name="Enable Node Graph Tools",
        default=True,
        update=lambda self, _: BTK_AddonPreferences.on_toggle_register(
            self, "node_graph_tools")
    )

    enable_assets_browser: bpy.props.BoolProperty(
        name="Enable Asset Browser Shortcut",
        default=True,
        update=lambda self, _: BTK_AddonPreferences.on_toggle_register(
            self, "assets_browser")
    )

    def draw(self, context):
        layout = self.layout

        layout.prop(self, "enable_view_switcher")
        layout.prop(self, "enable_editor_tools")
        if self.enable_editor_tools:
            box = layout.box()
            box.label(text="Asset Browser Window Mode")
            box.prop(self, "asset_browser_window_mode")
            if self.asset_browser_window_mode == WindowMode.RENDER.name:
                row = box.row()
                row.prop(self, "asset_browser_window_mode_x")
                row.prop(self, "asset_browser_window_mode_y")
        layout.prop(self, "enable_object_tools")
        layout.prop(self, "enable_node_graph_tools")
        layout.prop(self, "enable_assets_browser")


def get_addon_prefs() -> BTK_AddonPreferences:
    return bpy.context.preferences.addons[addon_name].preferences


def get_current_asset_browser_window_mode() -> WindowMode:
    mode_name = get_addon_prefs().asset_browser_window_mode
    try:
        return WindowMode[mode_name]
    except KeyError:
        return WindowMode.RENDER


def get_current_asset_browser_window_size() -> tuple[int, int]:
    prefs = get_addon_prefs()
    return prefs.asset_browser_window_mode_x, prefs.asset_browser_window_mode_y
