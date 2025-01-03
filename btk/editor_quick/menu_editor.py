import bpy

from .clean_duplicated_textures import BITSYTK_OT_clean_duplicated_texture
from .clean_unused_material_slot import BITSYTK_OT_clean_unused_material_slot
from .open_asset_browser import BITSYTK_OT_open_asset_browser
from .rename_data_by_object_name import BITSYTK_OT_rename_data_by_object_name
from .rename_images_by_filename import BITSYTK_OT_rename_images_by_filename
from .rename_images_extension import BITSYTK_OT_rename_images_extension


class BITSYTK_MT_editor(bpy.types.Menu):
    bl_label = "Bitsy"

    def draw(self, context):
        layout = self.layout
        layout.operator(BITSYTK_OT_open_asset_browser.bl_idname)
        layout.menu(BITSYTK_MT_editor_clean.__name__)
        layout.menu(BITSYTK_MT_editor_rename.__name__)

    def menu_draw(self, context):
        self.layout.menu(BITSYTK_MT_editor.__name__)


class BITSYTK_MT_editor_clean(bpy.types.Menu):
    bl_label = "Clean"

    def draw(self, context):
        layout = self.layout
        layout.operator(BITSYTK_OT_clean_unused_material_slot.bl_idname)
        layout.operator(BITSYTK_OT_clean_duplicated_texture.bl_idname)


class BITSYTK_MT_editor_rename(bpy.types.Menu):
    bl_label = "Rename"

    def draw(self, context):
        layout = self.layout
        layout.menu(BITSYTK_MT_editor_rename_images.__name__)
        layout.menu(BITSYTK_MT_editor_rename_objects.__name__)


class BITSYTK_MT_editor_rename_images(bpy.types.Menu):
    bl_label = "Images"

    extension: bpy.props.StringProperty()
    new_extension: bpy.props.StringProperty()

    def draw(self, context):
        layout = self.layout
        layout.operator(BITSYTK_OT_rename_images_by_filename.bl_idname)
        layout.separator()
        layout.operator(BITSYTK_OT_rename_images_extension.bl_idname)


class BITSYTK_MT_editor_rename_objects(bpy.types.Menu):
    bl_label = "Datas"

    def draw(self, context):
        layout = self.layout
        layout.operator(BITSYTK_OT_rename_data_by_object_name.bl_idname)
