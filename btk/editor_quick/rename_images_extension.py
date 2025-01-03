import bpy

from ..utilities import show_message_box


#################################################################################
# Operator
#################################################################################
class BITSYTK_OT_rename_images_extension(bpy.types.Operator):
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
        _rename_images_extension(self.extension, self.new_extension, bpy.data.images)
        return {"FINISHED"}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


#################################################################################
# Functions
#################################################################################
def _rename_images_extension(old_extension, new_extension, images):
    counter = 0
    for image in images:
        if old_extension not in image.filepath:
            continue
        image.filepath = image.filepath.replace(old_extension, new_extension)
        counter += 1
        image.reload()
    show_message_box(f"Renamed {counter} images", title="Result")
