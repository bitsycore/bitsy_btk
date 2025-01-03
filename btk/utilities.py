import bpy


############################################
# MARK: Materials
############################################


def get_all_materials() -> set[bpy.types.Material]:
    mats: set[bpy.types.Material] = set()

    mat: bpy.types.Material
    for mat in bpy.data.materials:
        if mat.name != "Dots Stroke":
            mats.add(mat)

    return mats


def get_all_materials_in_selected_objects() -> set[bpy.types.Material]:
    mats: set[bpy.types.Material] = set()

    obj: bpy.types.Object
    for obj in get_selected_objects():
        slot: bpy.types.MaterialSlot
        for slot in obj.material_slots:
            mats.add(slot.material)

    return mats


def get_all_materials_in_active_object() -> set[bpy.types.Material]:
    mats: set[bpy.types.Material] = set()

    slot: bpy.types.MaterialSlot
    for slot in bpy.context.active_object.material_slots:
        mats.add(slot.material)

    return mats


############################################
# MARK: Objects
############################################


def get_all_objects() -> set[bpy.types.Object]:
    return set(bpy.data.objects.values())


def get_selected_objects() -> set[bpy.types.Object]:
    return set(bpy.context.selected_objects)


def get_active_object() -> bpy.types.Object:
    return bpy.context.active_object


def show_message_box(message="", title="Info", icon="INFO"):
    bpy.context.window_manager.popup_menu(lambda self, a: self.layout.label(text=message), title=title, icon=icon)

    print("[" + title + "] : " + message)


############################################
# MARK: Assets Browser
############################################


def open_asset_browser_window():
    mode = 1

    # Use Render Window (Don't have Always On Top but is sizable)
    if mode == 1:
        render = bpy.context.scene.render
        prefs = bpy.context.preferences

        # Save Old Values
        old_dirty = prefs.is_dirty
        old_display_type = prefs.view.render_display_type
        old_x = render.resolution_x
        old_y = render.resolution_y
        old_percentage = render.resolution_percentage

        render.resolution_x = 1280
        render.resolution_y = 480
        render.resolution_percentage = 100
        prefs.view.render_display_type = "WINDOW"

        bpy.ops.render.view_show("INVOKE_DEFAULT")

        area = bpy.context.window_manager.windows[-1].screen.areas[0]
        area.ui_type = "ASSETS"

        # Restore Old Values
        render.resolution_x = old_x
        render.resolution_y = old_y
        render.resolution_percentage = old_percentage
        prefs.view.render_display_type = old_display_type
        prefs.is_dirty = old_dirty

    # Use Pref Window (Have Always On Top but is not sizable)
    elif mode == 2:
        bpy.ops.screen.userpref_show("INVOKE_DEFAULT")
        bpy.context.window.screen = bpy.context.window_manager.windows[-1].screen
        bpy.ops.screen.area_dupli()
        bpy.context.window.screen.areas[0].ui_type = "ASSETS"
