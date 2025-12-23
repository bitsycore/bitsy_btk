import bpy

from .window_mode import WindowMode


############################################
# MARK: Materials
############################################


def get_all_materials() -> set[bpy.types.Material]:
    return {mat for mat in bpy.data.materials.values() if mat != "Dots Stroke"}


def get_all_materials_in_selected_objects() -> set[bpy.types.Material]:
    return {slot.material for object in get_selected_objects() for slot in object.material_slots}


def get_all_materials_in_active_object() -> set[bpy.types.Material]:
    return {slot.material for slot in get_active_object().material_slots}


############################################
# MARK: Objects
############################################


def get_all_objects() -> set[bpy.types.Object]:
    return set(bpy.data.objects.values())


def get_selected_objects() -> set[bpy.types.Object]:
    return set(bpy.context.selected_objects)


def get_active_object() -> bpy.types.Object:
    return bpy.context.active_object


############################################
# MARK: Windows
############################################


def open_window(area_type: str, window_mode: WindowMode, width=1280, height=480):
    if window_mode == WindowMode.PREF:
        bpy.ops.screen.userpref_show("INVOKE_DEFAULT")
        bpy.context.window.screen = bpy.context.window_manager.windows[-1].screen
        bpy.ops.screen.area_dupli()
        bpy.context.window.screen.areas[0].ui_type = area_type

    elif window_mode == WindowMode.RENDER:
        render = bpy.context.scene.render
        prefs = bpy.context.preferences

        save_old_values = (
            prefs.is_dirty,
            prefs.view.render_display_type,
            render.resolution_x,
            render.resolution_y,
            render.resolution_percentage
        )

        # Custom Values
        render.resolution_x = width
        render.resolution_y = height
        render.resolution_percentage = 100
        prefs.view.render_display_type = "WINDOW"

        # Open Window and Set Area Type
        bpy.ops.render.view_show("INVOKE_DEFAULT")
        area = bpy.context.window_manager.windows[-1].screen.areas[0]
        area.ui_type = area_type

        # Restore Old Values
        prefs.is_dirty = save_old_values[0]
        prefs.view.render_display_type = save_old_values[1]
        render.resolution_x = save_old_values[2]
        render.resolution_y = save_old_values[3]
        render.resolution_percentage = save_old_values[4]

    elif window_mode == WindowMode.NEW:
        bpy.ops.wm.window_new("INVOKE_DEFAULT")
        bpy.context.window_manager.windows[-1].screen.areas[0].ui_type = area_type


############################################
# MARK: Others
############################################


def show_message_box(message="", title="Info", icon="INFO"):
    bpy.context.window_manager.popup_menu(
        lambda self, a: self.layout.label(text=message), title=title, icon=icon)
    print("[" + title + "] : " + message)
