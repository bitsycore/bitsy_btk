import bpy
from .preferences import BTK_AddonPreferences, get_addon_prefs
from . import editor_tools, view_switcher, asset_browser, object_tools, node_graph_tools

modules = {
    "editor_tools": editor_tools,
    "view_switcher": view_switcher,
    "asset_browser": asset_browser,
    "object_tools": object_tools,
    "node_graph_tools": node_graph_tools,
}


def update_module_registration(enabled: bool, module_name: str):
    module = modules.get(module_name)
    if module:
        (module.register if enabled else module.unregister)()


def register():
    bpy.utils.register_class(BTK_AddonPreferences)
    pref = get_addon_prefs()

    # Register Modules
    for name, module in modules.items():
        if getattr(pref, f"enable_{name}", False):
            module.register()

    pref.on_toggle = update_module_registration


def unregister():
    pref = get_addon_prefs()

    for name, module in modules.items():
        if getattr(pref, f"enable_{name}", False):
            module.unregister()

    bpy.utils.unregister_class(BTK_AddonPreferences)
