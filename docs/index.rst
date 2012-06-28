
Welcome to the TPy documentation!
=================================

TPy is a `Python <http://www.python.org>`_ library meant to ease the use of the 
`TargetProcess <http://www.targetprocess.com>`_ REST API.

.. code-block:: python
    :linenos:
    :emphasize-lines: 3,5,7
    import tpy
    # Authenticate with an API key...
    tp = tpy.TargetProcess('http://demo.tpondemand.com/',api_key=BLAH)
    # or Basic auth...
    tp = tpy.TargetProcess('http://demo.tpondemand.com/',username=admin,password=supersecret)
    # loop through our stories
    for story in tp.UserStories.all:
        print story.Id


Contribution
------------

If you find this software useful, please feel welcome and encouraged
to contribute with bug fixes, documentation or new features.

GitHub project: `http://github.com/JonnyFunFun/TPy
<http://github.com/JonnyFunFun/TPy>`_


License
-------

This software is made available as-is under the GNU General Public License.

TPy is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

TPy is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with TPy.  If not, see `http://www.gnu.org/licenses/<http://www.gnu.org/licenses/>`_.


Contents
========

.. toctree::
   :maxdepth: 2

   tpy.rst
       tpy.objects.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
