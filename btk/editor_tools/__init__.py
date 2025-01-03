import bpy

from .clean_duplicated_textures import BTK_OT_clean_duplicated_texture
from .clean_unused_material_slot import BTK_OT_clean_unused_material_slot
from .menu_editor import BTK_MT_editor, BTK_MT_editor_clean, BTK_MT_editor_rename, BTK_MT_editor_rename_images, BTK_MT_editor_rename_objects
from .open_asset_browser import BTK_OT_open_asset_browser
from .rename_data_by_object_name import BTK_OT_rename_data_by_object_name
from .rename_images_by_filename import BTK_OT_rename_images_by_filename
from .rename_images_extension import BTK_OT_rename_images_extension


classes = [
    # MENU EDITOR
    BTK_MT_editor,
    BTK_MT_editor_clean,
    BTK_MT_editor_rename,
    BTK_MT_editor_rename_images,
    BTK_MT_editor_rename_objects,
    # EDITOR open_asset_browser
    BTK_OT_open_asset_browser,
    # REMOVE
    BTK_OT_clean_unused_material_slot,
    BTK_OT_clean_duplicated_texture,
    # RENAME OBJECTS
    BTK_OT_rename_data_by_object_name,
    # RENAME IMAGES
    BTK_OT_rename_images_by_filename,
    BTK_OT_rename_images_extension,
]


def register():
    for c in classes:
        bpy.utils.register_class(c)

    bpy.types.TOPBAR_MT_editor_menus.append(BTK_MT_editor.menu_draw)


def unregister():
    bpy.types.TOPBAR_MT_editor_menus.remove(BTK_MT_editor.menu_draw)

    for c in reversed(classes):
        bpy.utils.unregister_class(c)
