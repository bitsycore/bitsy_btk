import bpy

from .clean_duplicated_textures import BITSYTK_OT_clean_duplicated_texture
from .clean_unused_material_slot import BITSYTK_OT_clean_unused_material_slot
from .menu_editor import BITSYTK_MT_editor, BITSYTK_MT_editor_clean, BITSYTK_MT_editor_rename, BITSYTK_MT_editor_rename_images, BITSYTK_MT_editor_rename_objects
from .open_asset_browser import BITSYTK_OT_open_asset_browser
from .rename_data_by_object_name import BITSYTK_OT_rename_data_by_object_name
from .rename_images_by_filename import BITSYTK_OT_rename_images_by_filename
from .rename_images_extension import BITSYTK_OT_rename_images_extension


classes = [
    # MENU EDITOR
    BITSYTK_MT_editor,
    BITSYTK_MT_editor_clean,
    BITSYTK_MT_editor_rename,
    BITSYTK_MT_editor_rename_images,
    BITSYTK_MT_editor_rename_objects,
    # EDITOR open_asset_browser
    BITSYTK_OT_open_asset_browser,
    # REMOVE
    BITSYTK_OT_clean_unused_material_slot,
    BITSYTK_OT_clean_duplicated_texture,
    # RENAME OBJECTS
    BITSYTK_OT_rename_data_by_object_name,
    # RENAME IMAGES
    BITSYTK_OT_rename_images_by_filename,
    BITSYTK_OT_rename_images_extension,
]


def register():
    for c in classes:
        bpy.utils.register_class(c)

    bpy.types.TOPBAR_MT_editor_menus.append(BITSYTK_MT_editor.menu_draw)


def unregister():
    bpy.types.TOPBAR_MT_editor_menus.remove(BITSYTK_MT_editor.menu_draw)

    for c in reversed(classes):
        bpy.utils.unregister_class(c)
