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

from tpy.objects import TargetProcessEntity, TargetProcessField
from tpy.objects.history import History


class Change(TargetProcessEntity):
    """A single change applied to Entity field."""
    singular = 'Change'
    plural   = 'Changes'

    fields = {
        "Id"			: TargetProcessField(type='id'),
        "Field"         : TargetProcessField(type=str,editable=False),
        "OldValue"      : TargetProcessField(type=str,editable=False),
        "NewValue"      : TargetProcessField(type=str,editable=False),
        "History"       : TargetProcessField(type='link',obj=History)
    }
