import bpy

from ..utilities import get_all_materials_in_selected_objects, show_message_box


class BTK_OT_images_unpack(bpy.types.Operator):
    """Unpack Images from Objects"""

    bl_idname = "bitsy_btk.images_unpack"
    bl_label = "Unpack"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.mode == "OBJECT"

    def menu_draw(self, context):
        self.layout.operator(BTK_OT_images_unpack.bl_idname)

    def execute(self, context):
        mats = get_all_materials_in_selected_objects()
        images = set()

        mat: bpy.types.Material
        for mat in mats:
            if mat.name != "Dots Stroke":

                node: bpy.types.ShaderNode
                for node in mat.node_tree.nodes:
                    if node.type != "TEX_IMAGE":
                        continue

                    node: bpy.types.ShaderNodeTexImage

                    if node.image in images:
                        continue
                    if node.image.packed_file is None:
                        continue

                    images.add(node.image)
                    node.image.unpack()

        show_message_box(f"Unpacked {len(images)} image(s)", title="Result")

        return {"FINISHED"}
