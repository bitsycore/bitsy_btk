import bpy

from .images_change_alpha_mode import BITSYTK_OT_images_change_alpha_mode
from .images_pack import BITSYTK_OT_images_pack
from .images_unpack import BITSYTK_OT_images_unpack


class BITSYTK_MT_view3d_object(bpy.types.Menu):
    bl_label = "Bitsy"

    def draw(self, context):
        self.layout.menu(BITSYTK_MT_view3d_object_images.__name__)

    def menu_draw(self):
        self.layout.separator()
        self.layout.menu(BITSYTK_MT_view3d_object.__name__)


class BITSYTK_MT_view3d_object_images(bpy.types.Menu):
    bl_label = "Images"

    def draw(self, context: bpy.types.Context):
        layout = self.layout
        layout.operator(BITSYTK_OT_images_change_alpha_mode.bl_idname)
        layout.operator(BITSYTK_OT_images_pack.bl_idname)
        layout.operator(BITSYTK_OT_images_unpack.bl_idname)
