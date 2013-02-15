# This file is part of the TPy TargetProcess API Wrapper.
# Copyright (C) 2013 Jonathan Enzinna
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

import unittest
import tpy


class BasicTests(unittest.TestCase):
	def setUp(self):
		pass
		
	def test_create_with_api_key(self):
		tp = tpy.TargetProcess('http://demo.tpondemand.com/',api_key='BLAH')
		self.assertIsNotNone(tp)

	def test_create_with_basic_auth(self):
		tp = tpy.TargetProcess('http://demo.tpondemand.com/',username='admin',password='supersecret')
		self.assertIsNotNone(tp)
		
	def test_validate_url(self):
		tp = None
		try:
			tp = tpy.TargetProcess('super_bad-url_stuff&!*',username='',password='')
		except TypeError:
			pass
		self.assertIsNone(tp)
		
	def test_validate_credentials(self):
		tp = None
		try:
			tp = tpy.TargetProcess('http://demo.tpondemand.com/')
		except TypeError:
			pass
		self.assertIsNone(tp)
		
	def test_basic_authentication_header(self):
		tp = tpy.TargetProcess('http://demo.tpondemand.com/',username='admin',password='supersecret')
		self.assertEqual(tp.DEFAULT_HEADERS['Authorization'],'Basic: YWRtaW46c3VwZXJzZWNyZXQ=') # Base64 user:pass
		

if __name__ == '__main__':
	unittest.main()