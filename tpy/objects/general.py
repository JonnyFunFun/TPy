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
from tpy.objects.entitytype import EntityType
from tpy.objects.generaluser import GeneralUser
from tpy.objects.project import Project
from tpy.objects.customfield import CustomField
from tpy.objects.message import Message
from tpy.objects.attachment import Attachment
from tpy.objects.history import History


class General(TargetProcessEntity):
    """Base entity for Assignable, Build, Impediment, Iteration, Program, Project, 
    Release, Test Case, Test Plan, Bug, Feature, Request, Task, Test Plan Run, 
    User Story"""
    singular = 'General'
    plural   = 'Generals'
    
    fields = {
            "Id"            	: TargetProcessField(type='id'),
            "Name"          	: TargetProcessField(type=str),
            "Description"   	: TargetProcessField(type=str),
            "StartDate"     	: TargetProcessField(type=datetime,null=True),
            "EndDate"       	: TargetProcessField(type=datetime,null=True),
            "CreateDate"    	: TargetProcessField(type=datetime,editable=False,null=True),
            "ModifyDate"    	: TargetProcessField(type=datetime,null=True),
            "LastCommentDate"	: TargetProcessField(type=datetime,null=True),
            "Tags"          	: TargetProcessField(type=str,null=True),
			"NumericPriority"	: TargetProcessField(type=int),
            "IsNow"             : TargetProcessField(type=bool,editable=False),
            "IsNext"            : TargetProcessField(type=bool,editable=False),
            "IsPrevious"        : TargetProcessField(type=bool,editable=False),
			"EntityType"		: TargetProcessField(type='link',obj=EntityType),
            "Owner"         	: TargetProcessField(type='link',obj=GeneralUser),
			"LastCommentedUser"	: TargetProcessField(type='link',obj=GeneralUser),
            "Project"       	: TargetProcessField(type='link',obj=Project),
			"CustomFields"		: TargetProcessField(type='collection',obj=CustomField),
            "Comments"      	: TargetProcessField(type='collection',obj=Comment),
			"Messages"			: TargetProcessField(type='collection',obj=Message,editable=False),
			"TagObjects"		: TargetProcessField(type='collection',obj=Tag),
            "MasterRelations"   : TargetProcessField(type='collection',obj=Relation),
            "SlaveRelations"    : TargetProcessField(type='collection',obj=Relation),
            "Attachments"   	: TargetProcessField(type='collection',obj=Attachment),
			"Histories"			: TargetProcessField(type='collection',obj=History)
    }
        