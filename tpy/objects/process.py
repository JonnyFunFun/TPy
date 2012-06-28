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
from tpy.objects import *

class Process(TargetProcessEntity):
    """Set of practices that can be applied to a project. It is possible to 
    create custom processes with defined set of Practice."""
    singular = Process
    plural   = Processes
    
    fields = [
            "Id"            : TargetProcessField(type='id'),
            "Name"          : TargetProcessField(type=str),
            "Description"   : TargetProcessField(type=str),
            "EntityStates"  : TargetProcessField(type='collection',obj=EntityState)
        ]        