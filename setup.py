import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


version = re.search("__version__ = '([^']+)'",
                    open('tpy/__init__.py').read()).group(1)


setup(
    name='tpy',
    version=version,
    author='Jonathan Enzinna',
    author_email='jonathan@enzinna.com',
    maintainer='Jonathan Enzinna',
    maintainer_email='jonathan@enzinna.com',
    url='https://github.com/JonnyFunFun/TPy',
    description='A wrapper for the TargetProcess API',
    long_description=('Please see the `documentation on github '
                      '<https://github.com/JonnyFunFun/TPy>`_.'),
    classifiers=['Development Status :: 2 - Pre-Alpha',
                 'Environment :: Console',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: GNU General Public License (GPL)',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.2',
                 'Topic :: Utilities'],
    license='GPLv3',
    keywords=['api', 'targetprocess'],
    packages=['tpy'],
    package_data={'': ['COPYING'], 'tpy': ['*.cfg']},
    install_requires=['six'])