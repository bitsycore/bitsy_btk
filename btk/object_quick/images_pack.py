import bpy

from ..utilities import get_all_materials_in_selected_objects, show_message_box


class BTK_OT_images_pack(bpy.types.Operator):
    """Pack Images from Objects"""

    bl_idname = "bitsy_btk.images_pack"
    bl_label = "Pack"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.mode == "OBJECT"

    def menu_draw(self, context):
        self.layout.operator(BTK_OT_images_pack.bl_idname)

    def execute(self, context):
        mats = get_all_materials_in_selected_objects()
        images: set[bpy.types.Image] = set()

        mat: bpy.types.Material
        for mat in mats:
            if mat.name != "Dots Stroke":

                node: bpy.types.ShaderNode
                for node in mat.node_tree.nodes:
                    if node.type != "TEX_IMAGE":
                        continue
                    if node.image in images:
                        continue

                    node: bpy.types.ShaderNodeTexImage

                    images.add(node.image)
                    node.image.pack()

        show_message_box(f"Packed {len(images)} image(s)", title="Result")
        return {"FINISHED"}
