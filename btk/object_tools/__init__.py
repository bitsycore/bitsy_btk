import bpy

from .images_change_alpha_mode import BTK_OT_images_change_alpha_mode
from .images_pack import BTK_OT_images_pack
from .images_unpack import BTK_OT_images_unpack
from .menu_view3d_object import BTK_MT_view3d_object, BTK_MT_view3d_object_images


classes = (
    # IMAGES
    BTK_OT_images_change_alpha_mode,
    BTK_OT_images_pack,
    BTK_OT_images_unpack,
    # MENU
    BTK_MT_view3d_object,
    BTK_MT_view3d_object_images,
)


registered = False


def register():
    global registered
    if registered:
        return

    for c in classes:
        bpy.utils.register_class(c)

    bpy.types.VIEW3D_MT_object.append(BTK_MT_view3d_object.menu_draw)
    bpy.types.VIEW3D_MT_object_context_menu.append(
        BTK_MT_view3d_object.menu_draw)

    registered = True


def unregister():
    global registered
    if not registered:
        return

    bpy.types.VIEW3D_MT_object_context_menu.remove(
        BTK_MT_view3d_object.menu_draw)
    bpy.types.VIEW3D_MT_object.remove(BTK_MT_view3d_object.menu_draw)

    for c in reversed(classes):
        bpy.utils.unregister_class(c)

    registered = False
