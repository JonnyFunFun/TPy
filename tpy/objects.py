# This file is part of the TPy TargetProcess API Wrapper.
# Copyright (C) 2014 Jonathan Enzinna
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
from tpy.exceptions import *
import os
import glob


class TargetProcessEntity(object):
    """Base class representing an entity within TargetProcess"""
    _id = None
    _is_dirty = False

    def __setattr__(self, item, value):
        if not hasattr(self, item):
            raise AttributeError("'%s' entity has no attribute '%s'" % (self.__name__, item))
        
        super(TargetProcessEntity, self).__setattr__("_is_dirty", True)
        
        attr = getattr(self, item)        
        
        if isinstance(attr, Field):
            attr.set(value)
        else:
            super(TargetProcessEntity, self).__setattr__(item, value)
    
    def __getattribute__(self, item):
        attr = super(TargetProcessEntity, self).__getattribute__(item)
        if isinstance(attr, Field):
            return attr.value
        else:
            return attr            
        
    @property
    def id(self):
        return self._id
    
    @property
    def new(self):
        return self._id is None
    
    @property
    def url(self):
        return "/api/v1/%s/%s" % (self.Meta.plural, self.id or "")

    @property
    def is_dirty(self):
        return self._is_dirty
    
    @classmethod
    def all():
        pass
    
    @classmethod
    def get(entity_id):
        pass
    
    @classmethod
    def create(entity):
        pass


class Field(object):
    """An object to represent the settings for an entity attribute."""

    def __init__(self, type='uneditable', options=None, **kwargs):
        self.type = type
        self.value = None
        self.options = options
        self.editable = kwargs.pop('editable', True)
        self.getable = kwargs.pop('getable', True)
        self.null = kwargs.pop('null', False)
        self.obj = kwargs.pop('obj', None)
        self.enumerations = kwargs.pop('enum', None)
        # have to do this to bypass __setattr__ below
        object.__setattr__(self, 'value', kwargs.pop('value', self.default))
    
    def set(self, val):
        if not self.editable:
            raise ReadOnlyAttributeException(None)        
        # validation
        if type(val) == str and self.type not in [str, int, object, 'enum']:
            raise TypeError()
        elif type(val) == int and self.type not in [str, 'id', int, object]:
            raise TypeError()
        if self.type is 'enum' and val not in self.enumerations:
            raise ValueError()
        if val is None and not self.null:
            raise TypeError()
        if self.type is 'collection' and type(val) is not dict:
            raise TypeError()
        # Type conversion, if necessary
        if self.type is str:
            val = str(val)
        if self.type is int and isinstance(value, str):
            val = int(val)        
        self.value = val

    def __str__(self):
        return str(self.value or self.default)

    def __eq__(self, other):
        try:
            if isinstance(other, self.__class__):
                return self.value == other.value
            elif isinstance(other, str):
                if self.type == str:
                    return self.value == other
                else:
                    return self.__str__() == other
            elif isinstance(other, int):
                if self.type == int:
                    return self.value == other
                else:
                    return int(self.value) == other
            elif isinstance(other, datetime):
                if self.type == datetime:
                    return self.value == other
            elif isinstance(other, object):
                return self.__dict__ == other.__dict__
        except:
            return False
        return super(Field, self).__eq__(other)
    
    @property
    def is_getable(self):
        """Boolean flag for whether not this field is receivable from the API"""
        return self.getable
    
    @property
    def is_editable(self):
        """Boolean flag for whether or not this field is editable"""
        return self.type not in ('id', 'collection') and self.editable
    
    @property
    def default(self):
        """Return the default value for this data type (e.g. '' or [])"""

        if self.type in ('id', 'uneditable', 'enum') or self.null:
            return None
        elif self.type == 'collection':
            return []
        elif self.type == 'link':
            return self.obj()
        elif self.type == datetime:
            return datetime.now()
        else:
            return self.type()


class General(TargetProcessEntity):
    """Base entity for Assignable, Build, Impediment, Iteration, Program, Project, 
    Release, Test Case, Test Plan, Bug, Feature, Request, Task, Test Plan Run, 
    User Story"""
    
    class Meta():        
        singular = 'General'
        plural   = 'Generals'
    
    Name = Field(type=str)
    Description = Field(type=str)
    StartDate = Field(type=datetime,null=True)
    EndDate = Field(type=datetime,null=True)
    CreateDate = Field(type=datetime,editable=False,null=True)
    ModifyDate = Field(type=datetime,null=True)
    LastCommentDate = Field(type=datetime,null=True)
    Tags = Field(type=str,null=True)
    NumericPriority = Field(type=int)
    IsNow = Field(type=bool,editable=False)
    IsNext = Field(type=bool,editable=False)
    IsPrevious = Field(type=bool,editable=False)


class Assignable(General):
    pass