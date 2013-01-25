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
from tpy import TargetProcess
from tpy.exceptions import *
from xml.etree import ElementTree

class TargetProcessEntity(object):
    """Base class representing an entity within TargetProcess"""
    _id = None
    base = None
    singular = None
    plural = None
    fields = {}
    _is_dirty = False

    def __init__(self):
        if self.base is not None:
            self.fields.update(self.base.fields)

    def __setattr__(self, item, value):
        self._is_dirty = True
        super(self,object).__setattr__(item, value)

    @property
    def is_dirty(self):
        return self._is_dirty
    
    @classmethod
    def from_xml(cls, xml, parent=None):
        """Create a new object from XML data"""
        
        # instiantiate the object
        self = cls()
        
        for child in xml.getchildren():
            
            # convert the key to underscore notation for Python
            key = child.tag.replace('-', '_')
            
            # if this key is not recognized ignore it
            if key not in cls.fields:
                continue
        
            # if there is no data, just set the default
            if child.text == None:
                self.__dict__[key] = self.fields[key].default
                continue

            # if this an element with children, it's an object relationship
            if len(child.getchildren()) > 0:
                
                # is this element an array of objects?
                if cls.fields[key].type == list:
                    items = []
                    for item in child.getchildren():
                        klass = getattr(sys.modules[__name__], child.tag)
                        items.append(klass.from_xml(item, parent=self))
                    self.__dict__[child.tag.replace('-', '_')] = items
                    continue
                
                # otherwise, let's treat it like a single object
                else:
                    klass = getattr(sys.modules[__name__], child.tag)
                    self.__dict__[child.tag.replace('-', '_')] = klass.from_xml(child, parent=self)
                    continue
                
            # get and convert attribute value based on type
            data_type = child.get('type')
            if data_type == 'integer':
                value = int(child.text)
            elif data_type == 'datetime':
                value = datetime.strptime(child.text, '%Y-%m-%dT%H:%M:%S')
            else:
                value = unicode(child.text)

            # add value to object dictionary
            self.__dict__[key] = value
                
        return self
    
    def save_xml(self, include_id=True, **kwargs):
        """Return the object XML for sending back to TargetProcess"""
        
        # create new XML object
        if 'base_element' not in kwargs:
            kwargs['base_element'] = self.singular
        xml = ElementTree.Element(kwargs['base_element'])
        
        extra_attrs = kwargs.get('extra_attrs', {})
        
        # if the id should be included and it is not None, add it first
        if include_id and 'id' in self.__dict__ and self.id != None:
            id_element = ElementTree.SubElement(xml, tag='id', attrib={'type': 'integer'})
            id_element.text = str(self.id)

        # now iterate over the editable attributes
        for field, settings in self.fields.iteritems():
            
            # get the value for this field, or pass if it is missing
            if field in self.__dict__:
                value = self.__dict__[field]
            else:
                continue
            
            # if the field is not editable, don't pass it
            if not settings.is_editable:
                continue
            
            # if the value is equal to the default, don't pass it
            if value == settings.default:
                continue
            
            # if the value is a TargetProcessEntity, insert the XML for it
            if isinstance(value, TargetProcessEntity):
                xml.insert(0, value.save_xml(include_id=True))
                continue            
            
            field_name = field.replace('_', '-') if not settings.force_key else settings.force_key
            extra_attrs_copy = extra_attrs if not settings.extra_attrs else settings.extra_attrs
            
            # insert the remaining single-attribute elements
            e = ElementTree.Element(field_name, **extra_attrs_copy)
            if isinstance(value, int):
                e.text = str(value)
            elif isinstance(value, list):
                if len(value) == 0:
                    continue
                for item in value:
                    e.insert(0, item.save_xml(include_id=True))
            elif isinstance(value, datetime):
                e.text = datetime.strftime(value, '%Y-%m-%dT%H:%M:%S')
            else:
                e.text = value
            xml.insert(0, e)

        # return the final XML Element object
        return xml
    
    def save(self):
        xml = self.save_xml()
        xml_str = ElementTree.tostring(xml)
        
        if not self._id:
            # We're a new object
            resp = TargetProcess.request(self.plural, method='POST', xml=xml_str)
        else:
            # Doing an update
            resp = TargetProcess.request('%s/%s' % {self.plural, self._id}, method='POST', xml=xml_str)
        new = self.from_xml(resp)
        self.__dict__ = new.__dict__
    
class TargetProcessField(object):
    """An object to represent the settings for an entity attribute."""

    def __init__(self, type='uneditable', options=None, **kwargs):
        self.type = type
        self.options = options
        self.editable = kwargs.pop('editable', True)
        self.getable = kwargs.pop('getable', True)
        self.null = kwargs.pop('null', False)
        self.obj = kwargs.pop('obj', None)
        self.enumerations = kwargs.pop('enum', None)
        
    def __set__(self, instance, value):
        # we obviously cannot edit something that isn't editable
        if not self.editable:
            raise ReadOnlyAttributeException(None)
        # validation
        if type(value) == str and self.type not in [str, object, 'enum']:
            raise TypeError()
        elif type(value) == int and self.type not in [str, 'id', int, object]:
            raise TypeError()
        if self.type is 'enum' and value not in self.enumerations:
            raise ValueError()
        if value is None and not self.null:
            raise TypeError()
        if self.type is 'collection' and type(value) is not dict:
            raise TypeError()
        self.value = value

    def __get__(self, instance, owner):
        return self.value or self.default
    
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
    
    @property
    def is_getable(self):
        """Boolean flag for whether not this field is receivable from the API"""
        return self.getable
    
    @property
    def is_editable(self):
        """Boolean flag for whether or not this field is editable"""
        return self.type not in ('id', 'collection') and self.editable
        