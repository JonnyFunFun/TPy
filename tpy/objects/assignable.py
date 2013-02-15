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

from datetime import datetime
from tpy.objects import TargetProcessEntity, TargetProcessField
from tpy.objects.general import General


class Assignable(TargetProcessEntity):
    """Base entity for User Story, Task, Bug, Test Plan Run, Feature, Request. 
       It can be assigned to people and has workflow."""
    singular = 'Assignable'
    plural   = 'Assignables'
    
    base = General
    
    fields = {
            "Effort"		: TargetProcessField(type=int),
            "EffortCompleted":TargetProcessField(type=int,editable=False),
            "EffortToDo"	: TargetProcessField(type=int,editable=False),
            "TimeSpent"	    : TargetProcessField(type=int,editable=False),
            "TimeRemain"	: TargetProcessField(type=int,editable=False),
            "LeadTime"		: TargetProcessField(type=int,editable=False),
            "CycleTime"		: TargetProcessField(type=int,editable=False),
            "Release"       : TargetProcessField(type='link',obj=Release),
            "Iteration"     : TargetProcessField(type='link',obj=Iteration),
            "Team"          : TargetProcessField(type='link',obj=Team),
            "Priority"      : TargetProcessField(type='link',obj=Priority),
            "EntityState"   : TargetProcessField(type='link',obj=EntityState),
            "AssignedUser"  : TargetProcessField(type='collection',obj=GeneralUser),
            "Assignments"   : TargetProcessField(type='collection',obj=Assignment),
            "Impediments"   : TargetProcessField(type='collection',obj=Impediment),
            "Times"         : TargetProcessField(type='collection',obj=Time),
            "RoleEfforts"   : TargetProcessField(type='collection',obj=RoleEffort),
            "Revisions"     : TargetProcessField(type='collection',obj=Revision)
    }
        