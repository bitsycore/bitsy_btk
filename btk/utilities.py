from enum import Enum
import bpy
from .. import __name__ as addon_name


############################################
# MARK: General
############################################


def get_addon_name() -> str:
    return addon_name


############################################
# MARK: Materials
############################################


def get_all_materials() -> set[bpy.types.Material]:
    return {mat for mat in bpy.data.materials.values() if mat.name != "Dots Stroke"}


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


class WindowMode(Enum):
    """
    RENDER  : Use Render Window (Don't have Always On Top but is sizable)\n
    PREF    : Use Preference Window (Have Always On Top but is not sizable)
    NEW     : Open a new window (Can't do much more)
    """

    RENDER = 1
    PREF = 2
    NEW = 3


def open_window(area_type: str, window_mode: WindowMode, width=1280, height=480):
    if window_mode == WindowMode.PREF:
        bpy.ops.screen.userpref_show("INVOKE_DEFAULT")
        bpy.context.window.screen = bpy.context.window_manager.windows[-1].screen
        bpy.ops.screen.area_dupli()
        bpy.context.window.screen.areas[0].ui_type = area_type

    elif window_mode == WindowMode.RENDER:
        render = bpy.context.scene.render
        prefs = bpy.context.preferences

        # Save Old Values
        old_dirty = prefs.is_dirty
        old_display_type = prefs.view.render_display_type
        old_x = render.resolution_x
        old_y = render.resolution_y
        old_percentage = render.resolution_percentage

        render.resolution_x = width
        render.resolution_y = height
        render.resolution_percentage = 100
        prefs.view.render_display_type = "WINDOW"

        bpy.ops.render.view_show("INVOKE_DEFAULT")
        area = bpy.context.window_manager.windows[-1].screen.areas[0]
        area.ui_type = area_type

        # Restore Old Values
        render.resolution_x = old_x
        render.resolution_y = old_y
        render.resolution_percentage = old_percentage
        prefs.view.render_display_type = old_display_type
        prefs.is_dirty = old_dirty

    elif window_mode == WindowMode.NEW:
        bpy.ops.wm.window_new("INVOKE_DEFAULT")
        bpy.context.window_manager.windows[-1].screen.areas[0].ui_type = area_type


############################################
# MARK: Assets Browser
############################################


def open_assets_browser_window(mode=WindowMode.PREF):
    open_window("ASSETS", mode)


############################################
# MARK: Others
############################################


def show_message_box(message="", title="Info", icon="INFO"):
    bpy.context.window_manager.popup_menu(lambda self, a: self.layout.label(text=message), title=title, icon=icon)
    print("[" + title + "] : " + message)
