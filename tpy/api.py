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

import sys, platform

__version__ = '0.0.1'

UA_STRING = '%%s TPy/%s Python/%s %s' % (__version__,
                                          sys.version.split()[0],
                                          platform.platform(True))

from six.moves import (http_cookiejar, http_client)
try:
    from urllib2 import HTTPCookieProcessor, build_opener
    import urlparse
except ImportError:
    from urllib import HttpCookieProcessor, build_opener, urlparse
import base64
import json
import os
import six
from tpy import objects


class TargetProcess(object):

    _username = None
    _password = None
    _api_key = None
    
    DEFAULT_HEADERS = {}
    RETRY_CODES = [502, 503, 504]
    BASE_URL = None
    
    def __init__(self, tp_url, api_key=None, username=None, password=None):
        """
        Create a connection to the TargetProcess instance residing at tp_url.
        
        Specify the authentication parameters for the connection to TargetProcess.  
        
        If using API key authentication, a username and password are not required.  
        If an api_key is not passed, a string representing the username and 
        password are required.
        """
        
        if not api_key and not username:
            raise TypeError('Either basic or API key credentials must be given.')

        if not api_key and (not isinstance(username, six.string_types) or not isinstance(password, six.string_types)):
            raise TypeError('Username and password must be strings')

        self._username = username
        self._password = password
        self._api_key = api_key
            
        self.DEFAULT_HEADERS['User-agent'] = UA_STRING
        
        self.BASE_URL = urlparse.urlparse(tp_url)
        if not self.BASE_URL.scheme in ['http','https']:
            raise TypeError('Unknown URL scheme')
        
        if not api_key:
            self.DEFAULT_HEADERS['Authorization'] = 'Basic: %s' % base64.b64encode(username+':'+password)

        _cookie_jar = http_cookiejar.CookieJar()
        self._opener = build_opener(HTTPCookieProcessor(_cookie_jar))

    def __str__(self):
        """
        String representation of the connection - basic stuff.
        """
	self.save()
        return 'Open TP Session (%s)' % (self._username or self._api_key)
    
    def __getattr__(self, k):
	if k[0] == '_':
	    raise AttributeError(k)
	
	try:
	    return self[k]
	except KeyError, err:
	    raise AttributeError(k)
	
    def __getitem__(self, k):
	try:
	    cls_ = getattr(objects, k)
	    return cls_
	except AttributeError, err:
	    raise AttributeError('TargetProcess API has no resource %s" % k')

    def request(url, method='GET', data=None):
	"""Sends a request to the Targetprocess API
	
	Returns dict"""
        self = TargetProcess()
        if not self._api_key or self._username:
            raise TypeError('Either basic or API key credentials must be given.')
    
    def save(self, entity):
	"""Save an entity in Targetprocess
	
	Creates a new entity if entity._id is None
	
	Returns Entity
	"""
	pass