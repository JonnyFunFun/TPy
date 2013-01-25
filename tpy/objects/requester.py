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
from tpy.objects import generaluser, role, company

class Requester(TargetProcessEntity):
    """Represents a requester."""
    singular = 'Requester'
    plural   = 'Requesters'
    
	base = GeneralUser

    fields = {
			"AvatarUri"				: TargetProcessField(type=str,null=True),
			"Phone"					: TargetProcessField(type=str,null=True),
			"Notes"					: TargetProcessField(type=str,null=True),
			"SourceType"			: TargetProcessField(type='enum',enum=['None','Mail','External','Internal']),
			"Company"				: TargetProcessField(type='link',obj=Company)
    }
