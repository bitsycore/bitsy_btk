import bpy


class BITSYTK_OT_center_nodetree(bpy.types.Operator):
    bl_idname = "bitsy_btk.center_nodes"
    bl_label = "Center Node Tree"
    bl_options = {"REGISTER", "UNDO"}

    target_objects = [
        ("ALL", "All", "Center for all nodetree"),
        ("CURRENT", "Current", "Center for current nodetree"),
    ]

    target: bpy.props.EnumProperty(items=target_objects, name="Target", description="Choose the target objects", default="ALL")

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.mode == "OBJECT"

    def invoke(self, context, _):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        if self.target == "ALL":
            _center_all_nodes()
        elif self.target == "CURRENT":
            if context.space_data.edit_tree:
                _center_nodes(context.space_data.edit_tree.nodes)
        return {"FINISHED"}


def _center_nodes(nodes):
    min_x = float("inf")
    max_x = float("-inf")
    min_y = float("inf")
    max_y = float("-inf")

    for node in nodes:
        if node.type == "FRAME":
            continue

        x, y = node.location
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    mid_x = (max_x + min_x) / 2
    mid_y = (max_y + min_y) / 2

    for node in nodes:
        if node.type == "FRAME":
            continue

        x, y = node.location
        node.location = (x - mid_x, y - mid_y)


def _center_all_nodes():
    # Center Materials
    for mat in bpy.data.materials:
        if mat.use_nodes:
            _center_nodes(mat.node_tree.nodes)

    # Center Worlds
    for world in bpy.data.worlds:
        if world.use_nodes:
            _center_nodes(world.node_tree.nodes)

    # Center Line styles
    for line_style in bpy.data.linestyles:
        if line_style.use_nodes:
            _center_nodes(line_style.node_tree.nodes)

    # Center Nodes Groups (Geometry Nodes, Groups etc...)
    for node_tree in bpy.data.node_groups:
        _center_nodes(node_tree.nodes)

    # Center Compositing NodeTree
    for scene in bpy.data.scenes:
        if scene.use_nodes:
            _center_nodes(scene.node_tree.nodes)

    # Center Compositing Textures
    for texture in bpy.data.textures:
        if texture.use_nodes:
            _center_nodes(texture.node_tree.nodes)
