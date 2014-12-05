# TPy

[![Build Status](https://travis-ci.org/JonnyFunFun/TPy.png?branch=master)](https://travis-ci.org/JonnyFunFun/TPy)

TPy is a Python wrapper for the [TargetProcess](http://www.targetprocess.com/) API.  
It is designed to make interfacing with the REST API easier.

*Please note:* TPy is currently under active development.  Features outlined in this README are incomplete, and 
instead represent the final vision for the wrapper.  This library is not ready for use.

```python
import tpy
# Authenticate with an API key...
tp = tpy.TargetProcess('http://demo.tpondemand.com/',api_key=BLAH)
# or Basic auth...
tp = tpy.TargetProcess('http://demo.tpondemand.com/',username=admin,password=supersecret)
# loop through our stories
for story in tp.UserStories.all:
    print story.Id
```

# Installation

You can install via `pip` 

    pip install tpy

Or via `easy-install`

    easy_install tpy

Or via `setup.py`

    python setup.py install
    
# Documentation

View the documentation at [http://tpy.readthedocs.org](http://tpy.readthedocs.org)

    
# License
All of the code contained here is licensed by the GNU GPLv3.
