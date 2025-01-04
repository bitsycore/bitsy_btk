import bpy
from ..utilities import open_window
from ..preferences import get_current_asset_browser_window_mode, get_current_asset_browser_window_size


class BTK_OT_open_asset_browser(bpy.types.Operator):
    """Open Asset Browser in a new window"""

    bl_idname = "bitsy_btk.open_window_asset_browser"
    bl_label = "Open Asset Browser"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return context.mode == "OBJECT"

    def execute(self, context):
        x, y = get_current_asset_browser_window_size()
        mode = get_current_asset_browser_window_mode()
        open_window("ASSETS", mode, x, y)
        return {"FINISHED"}
