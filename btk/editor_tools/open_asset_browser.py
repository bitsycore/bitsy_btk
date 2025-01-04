import bpy

from ..utilities import open_assets_browser_window


class BTK_OT_open_asset_browser(bpy.types.Operator):
    """Open Asset Browser in a new window"""

    bl_idname = "bitsy_btk.open_window_asset_browser"
    bl_label = "Open Asset Browser"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return context.mode == "OBJECT"

    def execute(self, context):
        open_assets_browser_window()
        return {"FINISHED"}
