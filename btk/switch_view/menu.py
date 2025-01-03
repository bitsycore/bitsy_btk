import bpy


def node_menu(self, context: bpy.types.Context):
    snode: bpy.types.Space = context.space_data
    layout: bpy.types.UILayout = self.layout

    row = layout.row(align=True)

    op = row.operator("wm.switch_editor", text="Mat", icon="NODE_MATERIAL", depress=snode.tree_type == "ShaderNodeTree")
    op.editor = "ShaderNodeTree"
    op = row.operator("wm.switch_editor", text="Geo", icon="GEOMETRY_NODES", depress=snode.tree_type == "GeometryNodeTree")
    op.editor = "GeometryNodeTree"
    op = row.operator("wm.switch_editor", text="Comp", icon="NODE_COMPOSITING", depress=snode.tree_type == "CompositorNodeTree")
    op.editor = "CompositorNodeTree"


def image_menu(self, context: bpy.types.Context):
    layout: bpy.types.UILayout = self.layout

    if context.space_data.mode != "UV":
        row = layout.row(align=True)
        op = row.operator("wm.switch_editor", text="", icon="UV")
        op.editor = "UV"
    else:
        row = layout.row(align=True)
        op = row.operator("wm.switch_editor", text="", icon="IMAGE")
        op.editor = "IMAGE_EDITOR"


def file_menu(self, context: bpy.types.Context):
    from bpy_extras.asset_utils import SpaceAssetInfo

    layout: bpy.types.UILayout = self.layout
    space_data: bpy.types.Space = context.space_data

    if SpaceAssetInfo.is_asset_browser(space_data):
        row = layout.row(align=True)
        op = row.operator("wm.switch_editor", text="", icon="FILEBROWSER")
        op.editor = "FILES"
    else:
        row = layout.row(align=True)
        op = row.operator("wm.switch_editor", text="", icon="ASSET_MANAGER")
        op.editor = "ASSETS"
