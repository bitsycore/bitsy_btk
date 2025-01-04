from . import btk


bl_info = {
    "name": "Bitsy Blender Toolkit",
    "description": "Utilities for Blender",
    "author": "Bitsy",
    "version": (1, 0, 1),
    "blender": (4, 2, 0),
    "location": "Editor > Bitsy",
    "support": "COMMUNITY",
    "category": "Utility",
}


def register():
    btk.register()


def unregister():
    btk.unregister()
