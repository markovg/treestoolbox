What is PyTREESTB
-----------------

This package allows you to use the excellent trees toolbox from within
Python.  MATLAB is required, as pytreestb uses pymatlab
(http://sourceforge.net/projects/pymatlab/) to exposes a Pythonic
wrapping of a bridge to the official trees MATLAB toolbox running in a
MATLAB session.

NB: TreesTB GUI functionality _is_ working.


License
-------

 Copyright (C) 2010 Eilif Muller <eilif.mueller@epfl.ch>

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.


See ./COPYING for the GPL3 license.


Installation
------------

PyTreesTB needs the svn version of PyMATLAB.  Install as follows ...

$ svn co https://pymatlab.svn.sourceforge.net/svnroot/pymatlab/trunk pymatlab 

In the newly checked out pymatlab-svn dir, configure your setup.cfg
from the templates provided, and run

$ sudo python setup.py install


Now you can install PyTREESTB

Set your TREESTB_HOME to the path to the TREES MATLAB source, which is available from http://code.google.com/p/treestoolbox/trunk/TREES.  For bash for example, put the following in you ~/.bashrc file:

$ export TREESTB_HOME=<path_to_dir_containing_TREES>


Now you're ready to install

$ sudo python setup.py install


You should then be able to:

$ python
>>> import pytreestb

The sub-modules are named the same as their MATLAB counterparts
(edit,IO,etc.), and contain their specific wrapped treestb functions.
The MATLAB docstrings are made available to the user:

$ ipython

In []: import pytreestb as ttb
In []: ttb.edit.resample_tree ?
... displays MATLAB help

In []: s = ttb.sample_tree()
In []: rs = ttb.edit.resample_tree(s,5)
In []: print rs




