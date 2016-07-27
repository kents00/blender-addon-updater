# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name":        "Addon Updater Demo",
    "description": "Demo addon for showcasing the blender-addon-updater module",
    "author":      "Patrick W. Crawford",
    "version":     (0, 2, 0),
    "blender":     (2, 7, 7),
    "location":    "View 3D > Tool Shelf > Demo Updater",
    "warning":     "",  # used for warning icon and text in addons panel
    "wiki_url":    "https://github.com/CGCookie/blender-addon-updater",
    "tracker_url": "https://github.com/CGCookie/blender-addon-updater/issues",
    "category":    "System"
    }


import bpy

# updater ops import
from . import addon_updater_ops # all setup in this file


# demo bare-bones preferences
class DemoPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    # addon updater preferences

    auto_check_update = bpy.props.BoolProperty(
        name = "Auto-check for Update",
        description = "If enabled, auto-check for updates using an interval",
        default = False,
        )
    
    updater_intrval_months = bpy.props.IntProperty(
        name='Months',
        description = "Number of months between checking for updates",
        default=0,
        min=0
        )
    updater_intrval_days = bpy.props.IntProperty(
        name='Days',
        description = "Number of days between checking for updates",
        default=14,
        min=0,
        )
    updater_intrval_hours = bpy.props.IntProperty(
        name='Hours',
        description = "Number of hours between checking for updates",
        default=0,
        min=0,
        max=23
        )
    updater_intrval_minutes = bpy.props.IntProperty(
        name='Minutes',
        description = "Number of minutes between checking for updates",
        default=0,
        min=0,
        max=59
        )

    def draw(self, context):
        
        layout = self.layout

        # updater draw function
        addon_updater_ops.update_settings_ui(self,context)


def register():

    # addon updater code and configurations
    addon_updater_ops.register(bl_info)

    # register the example panel, to show updater buttons
    bpy.utils.register_class(DemoPreferences)

    # TODO: create sample panel for background update checking demo


def unregister():

    # addon updater unregister
    addon_updater_ops.unregister()

    # register the example panel, to show updater buttons
    bpy.utils.unregister_class(DemoPreferences)

    # TODO: create sample panel for background update checking demo
