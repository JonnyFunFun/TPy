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

import inspect
import six
import sys

class TPyException(Exception):
    """Base exception class for errors that don't involve the remote API."""
    def __init__(self, message):
        super(TPyException, self).__init__()
        self.message = message

    def __str__(self):
        return self.message
        
class AuthenticationException(TPyException):
    """Exception thrown when authentication errors are encountered.