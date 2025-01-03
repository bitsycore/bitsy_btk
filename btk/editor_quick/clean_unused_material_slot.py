import bpy

from ..utilities import get_all_objects, show_message_box


class BTK_OT_clean_unused_material_slot(bpy.types.Operator):
    """Remove all unused material slot in the file"""

    bl_idname = "bitsy_btk.clean_unused_material_slot"
    bl_label = "Unused Materials slot"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.mode == "OBJECT"

    def execute(self, context):
        ob: bpy.types.Object
        for ob in get_all_objects():
            if not ob.material_slots:
                continue

            if ob.visible_get():
                with bpy.context.temp_override(active_object=ob):
                    bpy.ops.object.material_slot_remove_unused()

        show_message_box("Removed unused material slot", title="Result")
        return {"FINISHED"}
