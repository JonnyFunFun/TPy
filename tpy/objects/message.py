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
from tpy.objects import general, generaluser, attachment

class Message(TargetProcessEntity):
    """Email message from email integration."""
    singular = 'Message'
    plural   = 'Messages'
    
    fields = {
            "Id"		    : TargetProcessField(type='id'),
            "Subject"      : TargetProcessField(type=str),
            "Recipients"   : TargetProcessField(type=str)
            "Body"         : TargetProcessField(type=str),
            "IsRead"       : TargetProcessField(type=bool),
            "IsProcessed"  : TargetProcessField(type=bool),
            "CreateDate"   : TargetProcessField(type=datetime),
            "SendDate"     : TargetProcessField(type=datetime),
            "MessageType"  : TargetProcessField(type='enum',enum=['None','Inbox','Outbox','Public']),
            "ContentType"  : TargetProcessField(type='enum',enum=['None','Mail','Error','Email']),
            "From"         : TargetProcessField(type='link',obj=GeneralUser),
            "To"           : TargetProcessField(type='link',obj=GeneralUser),
            "MessageUid"   : TargetProcessField(type='link',obj=MessageUid),
            "Generals"     : TargetProcessField(type='collection',obj=General),
            "Attachment"   : TargetProcessField(type='collection',obj=Attachment)
    }
        