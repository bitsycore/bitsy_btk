import bpy


class NODE_OT_switch_editor(bpy.types.Operator):
    """Switch Editor"""

    bl_idname = "wm.switch_editor"
    bl_label = "Switch Editor"
    bl_options = {"REGISTER", "UNDO"}

    editor: bpy.props.StringProperty()

    def execute(self, context):
        bpy.ops.wm.context_set_enum(data_path="area.ui_type", value=self.editor)
        return {"FINISHED"}
