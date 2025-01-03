import bpy


############################################
# MARK: Materials
############################################


def get_all_materials():
    mats = set()
    for mat in bpy.data.materials:
        if mat.name != "Dots Stroke":
            mats.add(mat)
    return mats


def get_all_materials_in_selected_objects():
    mats = set()
    obj: bpy.types.Object
    for obj in get_selected_objects():
        for slot in obj.material_slots:
            mats.add(slot.material)
    return mats


def get_all_materials_in_active_object():
    mats = set()
    obj: bpy.types.Object = bpy.context.active_object
    for slot in obj.material_slots:
        mats.add(slot.material)
    return mats


############################################
# MARK: Objects
############################################


def get_all_objects():
    return bpy.data.objects


def get_selected_objects():
    objects = set()
    for obj in bpy.context.selected_objects:
        objects.add(obj)
    return objects


def get_scene_object(scene: bpy.types.Scene):
    return scene.objects


def show_message_box(message="", title="Info", icon="INFO"):
    bpy.context.window_manager.popup_menu(lambda self, a: self.layout.label(text=message), title=title, icon=icon)

    print("[" + title + "] : " + message)
