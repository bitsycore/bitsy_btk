import bpy

from .images_change_alpha_mode import BTK_OT_images_change_alpha_mode
from .images_pack import BTK_OT_images_pack
from .images_unpack import BTK_OT_images_unpack


class BTK_MT_view3d_object(bpy.types.Menu):
    bl_label = "Bitsy"

    def draw(self, context):
        self.layout.menu(BTK_MT_view3d_object_images.__name__)

    def menu_draw(self, context):
        self.layout.separator()
        self.layout.menu(BTK_MT_view3d_object.__name__)


class BTK_MT_view3d_object_images(bpy.types.Menu):
    bl_label = "Images"

    def draw(self, context):
        layout = self.layout
        layout.operator(BTK_OT_images_change_alpha_mode.bl_idname)
        layout.operator(BTK_OT_images_pack.bl_idname)
        layout.operator(BTK_OT_images_unpack.bl_idname)
