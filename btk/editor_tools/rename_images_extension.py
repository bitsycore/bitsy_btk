import bpy

from ..utilities import show_message_box


class BTK_OT_rename_images_extension(bpy.types.Operator):
    """Rename images extension"""

    bl_idname = "bitsy_btk.rename_images_extension"
    bl_label = "Rename Images Extension"
    bl_options = {"REGISTER", "UNDO"}

    extension: bpy.props.StringProperty(
        name="Extension",
        description="Enter the extension to rename from",
        default="",
    )

    new_extension: bpy.props.StringProperty(
        name="New Extension",
        description="Enter the new extension",
        default="",
    )

    @classmethod
    def poll(cls, context):
        return context.mode == "OBJECT"

    def execute(self, context):
        counter = 0
        for image in bpy.data.images:
            if self.extension not in image.filepath:
                continue
            image.filepath = image.filepath.replace(self.extension, self.new_extension)
            counter += 1
            image.reload()
        show_message_box(f"Renamed {counter} images", title="Result")
        return {"FINISHED"}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
