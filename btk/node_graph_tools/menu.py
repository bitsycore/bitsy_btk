import bpy

from .operator import BTK_OT_center_nodetree


class BTK_MT_node(bpy.types.Menu):
    bl_label = "Bitsy"

    def draw(self, _):
        layout = self.layout
        layout.operator(BTK_OT_center_nodetree.bl_idname)

    def menu_draw(self, _):
        self.layout.menu(BTK_MT_node.__name__)
