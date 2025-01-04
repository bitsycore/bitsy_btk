import bpy

from .menu import BTK_MT_node
from .operator import BTK_OT_center_nodetree

classes = [
    # MENU
    BTK_MT_node,
    # OPERATOR
    BTK_OT_center_nodetree,
]


registered = False


def register():
    global registered
    if registered:
        return

    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.NODE_MT_editor_menus.append(BTK_MT_node.menu_draw)

    registered = True


def unregister():
    global registered
    if not registered:
        return

    bpy.types.NODE_MT_editor_menus.remove(BTK_MT_node.menu_draw)
    for c in reversed(classes):
        bpy.utils.unregister_class(c)

    registered = False
