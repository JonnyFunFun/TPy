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
from tpy.objects.general import General



class Release(TargetProcessEntity):
    """Delivering an increment(s) of product functionality to public. Release contains several Iterations."""
    singular = 'Release'
    plural   = 'Releases'
    
    base = General
    
    fields = {
            "IsCurrent"     : TargetProcessField(type=bool,editable=False),
            "Units"         : TargetProcessField(type=str,editable=False),
            "Features"      : TargetProcessField(type='collection',obj=Feature),
            "UserStories"   : TargetProcessField(type='collection',obj=UserStory),
            "Tasks"         : TargetProcessField(type='collection',obj=Tasks),
            "Bugs"          : TargetProcessField(type='collection',obj=Bugs),
            "TestPlanRuns"  : TargetProcessField(type='collection',obj=TestPlanRuns),
            "Requests"      : TargetProcessField(type='collection',obj=Requests),
            "Builds"        : TargetProcessField(type='collection',obj=Build)
    }
        