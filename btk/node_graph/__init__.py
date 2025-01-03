import bpy

from .menu import BTK_MT_node
from .operator import BTK_OT_center_nodetree

classes = [
    # MENU
    BTK_MT_node,
    # OPERATOR
    BTK_OT_center_nodetree,
]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.NODE_MT_editor_menus.append(BTK_MT_node.menu_draw)


def unregister():
    bpy.types.NODE_MT_editor_menus.remove(BTK_MT_node.menu_draw)
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
