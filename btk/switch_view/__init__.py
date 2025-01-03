import bpy

from .operator import NODE_OT_switch_editor
from .menu import node_menu, image_menu, file_menu

classes = [
    # Operators
    NODE_OT_switch_editor
]


def register():
    for c in classes:
        bpy.utils.register_class(c)

    bpy.types.NODE_HT_header.prepend(node_menu)
    bpy.types.IMAGE_HT_header.prepend(image_menu)
    bpy.types.FILEBROWSER_HT_header.prepend(file_menu)


def unregister():
    bpy.types.FILEBROWSER_HT_header.remove(file_menu)
    bpy.types.IMAGE_HT_header.remove(image_menu)
    bpy.types.NODE_HT_header.remove(node_menu)

    for c in reversed(classes):
        bpy.utils.unregister_class(c)