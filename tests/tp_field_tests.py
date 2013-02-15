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
from tpy.objects import TargetProcessField
from tpy.exceptions import ReadOnlyAttributeException


class BasicObjectTests(unittest.TestCase):
    def setUp(self):
        self._field = None

    def test_string_field_default(self):
        self._field = TargetProcessField(type=str)
        self.assertEqual(self._field, str())

    def test_string_field_values(self):
        self._field = TargetProcessField(type=str)
        self._field.value = "test"
        self.assertIsInstance(self._field, TargetProcessField)
        self.assertEqual(self._field, "test")

    def test_string_type_coersion(self):
        self._field = TargetProcessField(type=str)
        self._field.value = 10
        self.assertIsInstance(self._field, TargetProcessField)
        self.assertEqual(self._field, "10")

    def test_uneditable_field(self):
        self._field = TargetProcessField(type=str, editable=False)
        threw_exception = False
        try:
            self._field.value = "test"
        except ReadOnlyAttributeException:
            threw_exception = True
        self.assertIsNot(self._field, "test")
        self.assertTrue(threw_exception)

    def test_integer_field_default(self):
        self._field = TargetProcessField(type=int)
        self.assertEqual(self._field, int())

    def test_integer_field_values(self):
        self._field = TargetProcessField(type=int)
        self._field.value = 10
        self.assertIsInstance(self._field, TargetProcessField)
        self.assertEqual(self._field, 10)

    def test_integer_bad_value_type(self):
        self._field = TargetProcessField(type=int)
        threw_exception = False
        try:
            self._field.value = "test"
        except ValueError:
            threw_exception = True
        self.assertIsNot(self._field, "test")
        self.assertTrue(threw_exception)

    def test_enum_field_type(self):
        self._field = TargetProcessField(type='enum',enum=['one','two','three'])
        self.assertIsInstance(self._field, TargetProcessField)

    def test_enum_field_default(self):
        self._field = TargetProcessField(type='enum',enum=['one','two','three'])
        self.assertEqual(self._field, str(None))

    def test_enum_field_set_valid(self):
        self._field = TargetProcessField(type='enum',enum=['one','two','three'])
        self._field.value = 'two'
        self.assertEqual(self._field, 'two')

    def test_enum_field_set_invalid(self):
        self._field = TargetProcessField(type='enum',enum=['one','two','three'])
        threw_exception = False
        try:
            self._field.value = 'four'
        except ValueError:
            threw_exception = True
        self.assertIsNot(self._field, 'four')
        self.assertTrue(threw_exception)

if __name__ == '__main__':
    unittest.main()