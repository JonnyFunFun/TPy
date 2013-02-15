# This file is part of the TPy TargetProcess API Wrapper.
# Copyright (C) 2013 Jonathan Enzinna
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
from tpy.objects.relation import Relation


class RelationType(TargetProcessEntity):
    """Type of relation between Entities."""
    singular = 'RelationType'
    plural   = 'RelationTypes'
    
    fields = {
            "Id"            : TargetProcessField(type='id'),
            "Name"          : TargetProcessField(type=str),
            "Relations"     : TargetProcessField(type='collection',obj=Relation)
    }