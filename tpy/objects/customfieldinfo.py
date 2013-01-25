# This file is part of the TPy TargetProcess API Wrapper.
# Copyright (C) 2012 Jonathan Enzinna
#
# TPy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with TPy.  If not, see <http://www.gnu.org/licenses/>.

from tpy.objects import TargetProcessEntity
from tpy.objects import process

class CustomFieldInfo(TargetProcessEntity):
    """Information about custom field in a Process."""
    singular = 'CustomFieldInfo'
    plural   = 'CustomFieldInfos'
    
    fields = {
            "Id"            : TargetProcessField(type='id'),
			"EntityKind"	: TargetProcessField(type='link',obj=EntityKind,editable=False),
            "Name"          : TargetProcessField(type=str,editable=False),
			"Type"			: TargetProcessField(type='enum',enum=['None','Text','DropDown','CheckBox','URL','Date','RichText','Number','Entity'],editable=False),
			"Required"		: TargetProcessField(type=bool,editable=False),
			"Listed"		: TargetProcessField(type=bool,editable=False)
    }