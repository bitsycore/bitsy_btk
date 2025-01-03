import bpy

from .operator import BITSYTK_OT_center_nodetree


class BITSYTK_MT_node(bpy.types.Menu):
    bl_label = "Bitsy"

    def draw(self, _):
        layout = self.layout
        layout.operator(BITSYTK_OT_center_nodetree.bl_idname)

    def menu_draw(self, _):
        self.layout.menu(BITSYTK_MT_node.__name__)
