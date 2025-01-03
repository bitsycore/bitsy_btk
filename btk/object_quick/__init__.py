import bpy

from .images_change_alpha_mode import BITSYTK_OT_images_change_alpha_mode
from .images_pack import BITSYTK_OT_images_pack
from .images_unpack import BITSYTK_OT_images_unpack
from .menu_view3d_object import BITSYTK_MT_view3d_object, BITSYTK_MT_view3d_object_images


classes = (
    # IMAGES
    BITSYTK_OT_images_change_alpha_mode,
    BITSYTK_OT_images_pack,
    BITSYTK_OT_images_unpack,
    # MENU
    BITSYTK_MT_view3d_object,
    BITSYTK_MT_view3d_object_images,
)


def register():
    for c in classes:
        bpy.utils.register_class(c)

    bpy.types.VIEW3D_MT_object.append(BITSYTK_MT_view3d_object.menu_draw)
    bpy.types.VIEW3D_MT_object_context_menu.append(BITSYTK_MT_view3d_object.menu_draw)


def unregister():
    bpy.types.VIEW3D_MT_object_context_menu.remove(BITSYTK_MT_view3d_object.menu_draw)
    bpy.types.VIEW3D_MT_object.remove(BITSYTK_MT_view3d_object.menu_draw)

    for c in reversed(classes):
        bpy.utils.unregister_class(c)
