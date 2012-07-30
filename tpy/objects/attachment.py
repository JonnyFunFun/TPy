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
from tpy.objects import general, generaluser, message

class Attachment(TargetProcessEntity):
    """A file (image, archive, whatever) attached to Entity."""
    singular = 'Attachment'
    plural   = 'Attachments'
    
    fields = {
            "Id"		    : TargetProcessField(type='id'),
            "Name"         : TargetProcessField(type=str),
            "Description"  : TargetProcessField(type=str),
            "Date"         : TargetProcessField(type=datetime,editable=False),
            "MimeType"     : TargetProcessField(type=str,editable=False),
            "Uri"          : TargetProcessField(type=str,editable=False),
            "ThumbnailUri" : TargetProcessField(type=str,editable=False),
            "Size"         : TargetProcessField(type=int,editable=False),
            "Owner"        : TargetProcessField(type='link',obj=GeneralUser),
            "General"      : TargetProcessField(type='link',obj=General),
            "Message"      : TargetProcessField(type='link',obj=Message)
    }
        