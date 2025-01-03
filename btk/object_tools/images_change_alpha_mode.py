import bpy

from ..utilities import get_all_materials_in_active_object, get_all_materials_in_selected_objects, show_message_box


class BTK_OT_images_change_alpha_mode(bpy.types.Operator):
    bl_idname = "bitsy_btk.images_change_alpha_mode"
    bl_label = "Change Alpha Mode"
    bl_options = {"REGISTER", "UNDO"}

    alpha_modes = [
        ("NONE", "None", "Set alpha mode to None"),
        ("CHANNEL_PACKED", "Packed", "Set alpha mode to Packed"),
        ("PREMUL", "Pre-multiplied", "Set alpha mode to Pre-multiplied"),
        ("STRAIGHT", "Straight", "Set alpha mode to Straight"),
    ]

    target_objects = [
        ("ALL", "All", "Change alpha mode for all objects"),
        ("SELECTED", "Selected", "Change alpha mode for selected objects"),
        ("ACTIVE", "Active", "Change alpha mode for active object"),
    ]

    alpha_mode: bpy.props.EnumProperty(items=alpha_modes, name="Alpha Mode", description="Choose the alpha mode", default="STRAIGHT")

    target: bpy.props.EnumProperty(items=target_objects, name="Target", description="Choose the target objects", default="SELECTED")

    @classmethod
    def poll(cls, context):
        return context.mode == "OBJECT"

    def menu_draw(self, context):
        self.layout.operator_context = "INVOKE_DEFAULT"
        self.layout.operator(BTK_OT_images_change_alpha_mode.bl_idname, text="Change Alpha Mode")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        mats = []

        if self.target == "ALL":
            mats = bpy.data.materials
        elif self.target == "SELECTED":
            mats = get_all_materials_in_selected_objects()
        elif self.target == "ACTIVE":
            mats = get_all_materials_in_active_object()

        images = set()
        for mat in mats:
            if mat.name != "Dots Stroke":
                for node in mat.node_tree.nodes:
                    if node.type != "TEX_IMAGE":
                        continue
                    if node.image in images:
                        continue
                    if node.image.alpha_mode == self.alpha_mode:
                        continue

                    images.add(node.image)
                    node.image.alpha_mode = self.alpha_mode

        show_message_box(f"Changed {len(images)} image(s) alpha mode", title="Result")
        return {"FINISHED"}
