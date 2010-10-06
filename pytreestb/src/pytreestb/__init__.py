##    Copyright (C) 2010 Eilif Muller <eilif.mueller@epfl.ch>
##
##    This program is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##     This program is distributed in the hope that it will be useful,
##     but WITHOUT ANY WARRANTY; without even the implied warranty of
##     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##     GNU General Public License for more details.
##
##     You should have received a copy of the GNU General Public License
##     along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os
import pymatlab
from pymatlab import Session, FuncWrap
from pytreestb.tree import Tree, matlab_tree_converter

# create trees modules on the fly from MATLAB TreeTB analogues
import new
import glob


trees_home = os.environ.get('TREESTB_HOME',None)

if not trees_home:
    raise ImportError, "Please set environment variable TREESTB_HOME to src root of treestoolbox (get it at treestoolbox.org)."

if not os.path.exists(os.path.join(trees_home,'start_trees.m')):
    raise ImportError, "You have set the TREESTB_HOME but it does not contain 'start_trees.m'.\nPlease check that your TREESTB_HOME points to the src root of the trees MATLAB toolbox,\ni.e. the directory containing 'start_trees.m'."
    


# Session setup
_session = Session("matlab -nosplash -nodesktop")
_session.path(append=[trees_home])
_session.run('start_trees')

__doc__="""
A Python wrapper for the Trees Toolbox


MATLAB Documentation

"""+_session.help('trees')


def _close_session():
    #print "Closing Trees MATLAB session."
    _session.close()
import atexit
atexit.register(_close_session)

import sys
__self__ = sys.modules[__name__]

modules = ['IO','edit','stacks','gui','graphtheory',
           'electrotonics','construct','graphical',
           'metrics','scheme']

def wrap_functions(names, converters, target_namespace):
    for name in names:
        f = _session.func_wrap(name,converters = converters)
        f.__doc__ = "Trees Toolbox Function MATLAB Documentation:\n\n"+_session.help(name)
        target_namespace.__setattr__(name,f)


# Standard converters 
_session.converters = [matlab_tree_converter, pymatlab.csc_matrix_converter]

def import_trees_module(name):
    # create module & add to this one
    mod_name = 'pytreestb.'+name
    mod = new.module(mod_name,
                     ("The Trees Toolbox '%s' module" % mod_name) +_session.help(name)) 
    __self__.__setattr__(name,mod)

    sys.modules[mod_name] = mod

    # find functions and add to module
    m_files = glob.glob(os.path.join(trees_home,name,'*.m'))
    func_names = [os.path.splitext(os.path.split(x)[-1])[0] for x in m_files]
    func_names.remove('Contents')
    wrap_functions(func_names,None,mod)


# process all Trees modules
for name in modules:
    import_trees_module(name)

# wrapping global names
global_functions = ['sample_tree']
wrap_functions(global_functions, None, __self__)
del global_functions

# Cleanup the namespace
del atexit

