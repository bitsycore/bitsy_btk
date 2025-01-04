import bpy

from .quick_open import (
    ASSETS_OT_CloseAssetBrowser,
    ASSETS_OT_OpenAssetBrowser,
    ASSETS_OT_SetBrowserParams,
    menu_action_close_asset,
    menu_action_open_asset,
    menu_action_set_params,
)


classes = (
    ASSETS_OT_OpenAssetBrowser,
    ASSETS_OT_CloseAssetBrowser,
    ASSETS_OT_SetBrowserParams,
)


registered = False


def register():
    global registered
    if registered:
        return

    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_HT_tool_header.append(menu_action_open_asset)
    bpy.types.FILEBROWSER_HT_header.append(menu_action_set_params)
    bpy.types.FILEBROWSER_HT_header.append(menu_action_close_asset)
    bpy.types.WindowManager.asset_browser_openned = bpy.props.IntProperty(
        default=0)

    registered = True


def unregister():
    global registered
    if not registered:
        return

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    bpy.types.VIEW3D_HT_tool_header.remove(menu_action_open_asset)
    bpy.types.FILEBROWSER_HT_header.remove(menu_action_set_params)
    bpy.types.FILEBROWSER_HT_header.remove(menu_action_close_asset)
    del bpy.types.WindowManager.asset_browser_openned

    registered = False
