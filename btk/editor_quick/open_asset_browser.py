import bpy


class BITSYTK_OT_open_asset_browser(bpy.types.Operator):
    """Open Asset Browser in a new window"""

    bl_idname = "bitsy_btk.open_window_asset_browser"
    bl_label = "Open Asset Browser"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return context.mode == "OBJECT"

    def execute(self, context):
        _open_asset_browser()
        return {"FINISHED"}


def _open_asset_browser():
    mode = 1

    # Use Render Window (Don't have Always On Top but is sizable)
    if mode == 1:
        render = bpy.context.scene.render
        prefs = bpy.context.preferences

        # Save Old Values
        old_dirty = prefs.is_dirty
        old_display_type = prefs.view.render_display_type
        old_x = render.resolution_x
        old_y = render.resolution_y
        old_percentage = render.resolution_percentage

        render.resolution_x = 1280
        render.resolution_y = 480
        render.resolution_percentage = 100
        prefs.view.render_display_type = "WINDOW"

        bpy.ops.render.view_show("INVOKE_DEFAULT")

        area = bpy.context.window_manager.windows[-1].screen.areas[0]
        area.ui_type = "ASSETS"

        # Restore Old Values
        render.resolution_x = old_x
        render.resolution_y = old_y
        render.resolution_percentage = old_percentage
        prefs.view.render_display_type = old_display_type
        prefs.is_dirty = old_dirty

    # Use Pref Window (Have Always On Top but is not sizable)
    elif mode == 2:
        bpy.ops.screen.userpref_show("INVOKE_DEFAULT")
        bpy.context.window.screen = bpy.context.window_manager.windows[-1].screen
        bpy.ops.screen.area_dupli()
        bpy.context.window.screen.areas[0].ui_type = "ASSETS"
