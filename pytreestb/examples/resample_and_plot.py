import pytreestb
from pytreestb.edit import resample_tree
from pytreestb.IO import ver_tree
from pytreestb.graphical import plot_tree
from pytreestb.graphtheory import BO_tree

# MATLAB session
M = pytreestb._session


t1 = pytreestb.sample_tree()
assert isinstance(t1,pytreestb.Tree)
assert ver_tree(t1)
t2 = resample_tree(t1,10)
assert isinstance(t2,pytreestb.Tree)
assert ver_tree(t2)

# Fig 1
M.figure()
plot_tree(t1, BO_tree(t1))
M.title('original')
M.shine()
M.colorbar()

# Fig 2 - resampled
M.figure()
plot_tree(t2, BO_tree(t2))
M.title('resampled - 10um')
M.shine()
M.colorbar()

