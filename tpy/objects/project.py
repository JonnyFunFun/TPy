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

class Project(TargetProcessEntity):
    """Core entity which contains releases, feature, user stories, bugs, etc."""
    singular = Project
    plural   = Projects
    
    fields = [
            "Id"            : TargetProcessField(type='id'),
            "Name"          : TargetProcessField(type=str),
            "Description"   : TargetProcessField(type=str),
            "StartDate"     : TargetProcessField(type=datetime,editable=False,null=True),
            "EndDate"       : TargetProcessField(type=datetime,editable=False,null=True),
            "CreateDate"    : TargetProcessField(type=datetime,editable=False,null=True),
            "ModifyDate"    : TargetProcessField(type=datetime,editable=False,null=True),
            "LastCommentDate":TargetProcessField(type=datetime,editable=False,null=True),
            "Tags"          : TargetProcessField(type=str,null=True),
            "Owner"         : TargetProcessField(type='link',obj=GeneralUser),
            "Project"       : TargetProcessField(type='link',obj=Project),
            "Comments"      : TargetProcessField(type='collection',obj=Comment),
            "Attachments"   : TargetProcessField(type='collection',obj=Attachments),
            "IsActive"      : TargetProcessField(type=bool),
            "IsProduct"     : TargetProcessField(type=bool),
            "Generals"      : TargetProcessField(type='collection',obj=General),
            "Program"       : TargetProcessField(type='link',obj=Program),
            "Features"      : TargetProcessField(type='collection',obj=Feature),
            "Releases"      : TargetProcessField(type='collection',obj=Release),
            "Iterations"    : TargetProcessField(type='collection',obj=Iteration),
            "UserStories"   : TargetProcessField(type='collection',obj=UserStory),
            "Tasks"         : TargetProcessField(type='collection',obj=Task),
            "Bugs"          : TargetProcessField(type='collection',obj=Bug),
            "TestCases"     : TargetProcessField(type='collection',obj=TestCase),
            "TestPlans"     : TargetProcessField(type='collection',obj=TestPlan),
            "Builds"        : TargetProcessField(type='collection',obj=Build),
            "Times"         : TargetProcessField(type='collection',obj=Time),
            "Revisions"     : TargetProcessField(type='collection',obj=Revision),
            "CustomActivities":TargetProcessField(type='collection',obj=CustomActivity),
            "Company"       : TargetProcessField(type='link',obj=Company)
        ]
        
