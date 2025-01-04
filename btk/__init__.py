import importlib
import bpy
from .preferences import BTK_AddonPreferences, get_addon_prefs

modules = [
    "editor_tools",
    "view_switcher",
    "assets_browser",
    "object_tools",
    "node_graph_tools"
]

imported_modules = {
    module: importlib.import_module(f".{module}", package=__name__) for module in modules
}


def update_module_registration(enabled: bool, module_name: str):
    module = imported_modules.get(module_name)
    if module:
        (module.register if enabled else module.unregister)()


def register():
    bpy.utils.register_class(BTK_AddonPreferences)

    pref = get_addon_prefs()

    for name, module in imported_modules.items():
        if getattr(pref, f"enable_{name}"):
            module.register()

    pref.on_toggle = update_module_registration


def unregister():
    pref = get_addon_prefs()

    for name, module in imported_modules.items():
        if getattr(pref, f"enable_{name}"):
            module.unregister()

    bpy.utils.unregister_class(BTK_AddonPreferences)
