import bpy


class ASSETS_OT_CloseAssetBrowser(bpy.types.Operator):
    bl_idname = "bitsy_btk.close_asset_browser"
    bl_label = "Close"
    bl_description = "Close the asset browser"

    def execute(self, context):
        screen = bpy.context.screen

        if len(screen.areas) == 1:
            num_windows = len(bpy.context.window_manager.windows)
            if num_windows != 1:
                bpy.ops.wm.window_close()
        else:
            bpy.ops.screen.area_close()

        bpy.context.window_manager.asset_browser_openned = 0
        return {"FINISHED"}


class ASSETS_OT_SetBrowserParams(bpy.types.Operator):
    bl_idname = "bitsy_btk.set_browser_params"
    bl_label = "Default"
    bl_description = "Open the first Asset Library"

    def execute(self, context):
        asset_library = bpy.context.preferences.filepaths.asset_libraries[0]
        for area in bpy.context.screen.areas:
            if area.ui_type == "ASSETS":
                if asset_library:
                    area.spaces.active.params.asset_library_ref = asset_library.name
        return {"FINISHED"}


class ASSETS_OT_OpenAssetBrowser(bpy.types.Operator):
    bl_idname = "bitsy_btk.open_asset_browser"
    bl_label = "Assets"
    bl_description = "Open the asset browser"

    def execute(self, context: bpy.types.Context):
        if bpy.context.window_manager.asset_browser_openned == 1:
            return {"CANCELLED"}

        areas = bpy.context.window.screen.areas[:]

        bpy.ops.screen.area_split(direction="HORIZONTAL", factor=0.30)

        for area in bpy.context.window.screen.areas:
            if area not in areas:
                area.ui_type = "ASSETS"
                bpy.context.window_manager.asset_browser_openned = 1
        return {"FINISHED"}


def menu_action_open_asset(self, context: bpy.types.Context):
    self.layout.operator(ASSETS_OT_OpenAssetBrowser.bl_idname, text=ASSETS_OT_OpenAssetBrowser.bl_label, icon="ASSET_MANAGER")


def menu_action_close_asset(self, context: bpy.types.Context):
    self.layout.operator(ASSETS_OT_CloseAssetBrowser.bl_idname, text=ASSETS_OT_CloseAssetBrowser.bl_label)


def menu_action_set_params(self, context: bpy.types.Context):
    self.layout.operator(ASSETS_OT_SetBrowserParams.bl_idname, text=ASSETS_OT_SetBrowserParams.bl_label)
