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
from tpy.objects import user, culture, projectinfo, teaminfo, processinfo

class Context(TargetProcessEntity):
    """Context contains information about logged User, Culture, selected Projects and Processes."""
    singular = 'Context'
    plural   = 'Contexts'
    
    fields = {
            "Id"		    	: TargetProcessField(type='id'),
			"Acid"				: TargetProcessField(type=str,editable=False),
			"Edition"			: TargetProcessField(type=str,editable=False),
			"Version"			: TargetProcessField(type=str,editable=False),
			"LoggedUser"		: TargetProcessField(type='link',obj=User,editable=False),
			"Culture"			: TargetProcessField(type='link',obj=Culture,editable=False),
			"SelectedProjects"	: TargetProcessField(type='collection',obj=ProjectInfo),
			"SelectedTeams"		: TargetProcessField(type='collection',obj=TeamInfo),
			"Process"			: TargetProcessField(type='collection',obj=ProcessInfo)
    }
