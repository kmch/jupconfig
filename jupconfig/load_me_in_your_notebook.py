"""
Set the level of logging messages displayed in the notebook; 
in order of decreasing verbosity:
TRACE, DEBUG, INFO, WARNING, ERROR, CRITICAL 
(or, respectively, 0, 10, 20, 30, 40, 50).
"""
from jupconfig.loggers import *
log_lvl(ERROR) # = log_lvl(40) = lll(ERROR) = lll(40)

# Automatically reload modules before execution
%load_ext autoreload
%autoreload 2