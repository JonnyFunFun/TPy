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
from tpy.objects import assignable, comment, request

class GeneralUser(TargetProcessEntity):
    """Base entity for User and Requester."""
    singular = 'GeneralUser'
    plural   = 'GeneralUsers'
    
    fields = {
            "Id"            : TargetProcessField(type='id'),
            "FirstName"     : TargetProcessField(type=str),
            "LastName"      : TargetProcessField(type=str),
            "Email"         : TargetProcessField(type=str),
            "Login"         : TargetProcessField(type=str),
            "CreateDate"    : TargetProcessField(type=datetime,editable=False),
            "ModifyDate"    : TargetProcessField(type=datetime),
            "DeleteDate"    : TargetProcessField(type=datetime,editable=False),
            "IsActive"      : TargetProcessField(type=bool),
            "IsAdministrator":TargetProcessField(type=bool),
            "Kind"          : TargetProcessField(type=str,editable=False),
            "Password"      : TargetProcessField(type=str,getable=False),
            "Assignables"   : TargetProcessField(type='collection',obj=Assignable),
            "Comments"      : TargetProcessField(type='collection',obj=Comment),
            "Requests"      : TargetProcessField(type='collection',obj=Request)
    }
        