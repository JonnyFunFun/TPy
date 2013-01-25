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

class CustomField(TargetProcessEntity):
    """Custom field is an entity state extension which is declared on a process level. 
		As a result entity can contain declared custom field values. Custom fields has 
		following types: Text, DropDown, CheckBox, Url, Date, RichText, Number, Entity. 
		See reference for more details."""
    singular = 'CustomField'
    plural   = 'CustomFields'
    
    fields = {
            "Name"		: TargetProcessField(type=str,editable=False),
            "Content"	: TargetProcessField(type=object)
    }