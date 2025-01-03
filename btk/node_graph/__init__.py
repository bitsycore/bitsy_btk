import bpy

from .menu import BITSYTK_MT_node
from .operator import BITSYTK_OT_center_nodetree

classes = [
    # MENU
    BITSYTK_MT_node,
    # OPERATOR
    BITSYTK_OT_center_nodetree,
]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.NODE_MT_editor_menus.append(BITSYTK_MT_node.menu_draw)


def unregister():
    bpy.types.NODE_MT_editor_menus.remove(BITSYTK_MT_node.menu_draw)
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
