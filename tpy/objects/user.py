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
from tpy.objects import TargetProcessEntity
from tpy.objects import generaluser, role

class User(TargetProcessEntity):
    """Base entity for User and Requester."""
    singular = 'User'
    plural   = 'Users'
    
	base = GeneralUser

    fields = {
			"AvatarUri"				: TargetProcessField(type=str,null=True),
			"WeeklyAvailableHours" 	: TargetProcessField(type=float,default=40),
			"CurrentAllocation" 	: TargetProcessField(type=int),
			"CurrentAvailableHours" : TargetProcessField(type=float),
			"AvailableFrom"			: TargetProcessField(type=datetime),
			"AvailableFutureAllocation" : TargetProcessField(type=int),
			"AvailableFutureHours"	: TargetProcessField(type=float),
			"IsObserver"			: TargetProcessField(type=bool,default=False),
			"Skills"				: TargetProcessField(type=str,null=True),
			"ActiveDirectoryName"	: TargetProcessField(type=str,null=True),
			"Role"					: TargetProcessField(type='link',obj=Role),
			"Times"					: TargetProcessField(type='collection',obj=Time),
			"Impediments"			: TargetProcessField(type='collection',obj=Impediments),
			"CustomActivities"		: TargetProcessField(type='collection',obj=CustomActivity),
			"Revisions"				: TargetProcessField(type='collection',obj=Revision),
			"TeamMembers"			: TargetProcessField(type='collection',obj=ProjectMember),
			"Milestones"			: TargetProcessField(type='collection',obj=Milestone)
    }
