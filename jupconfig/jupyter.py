"""
Load the content of this file in the jupyter notebook
using following commands:

import os
import jupconfig
%load {os.path.dirname(jupconfig.__file__)}/jupyter.py
"""

# Set aliases of frequently used jupyter magic commands
%alias_magic mi matplotlib -p inline
%alias_magic mn matplotlib -p notebook

# Set matplotlib backend (comment one or the other):
# - non-interactive plots displayed in a notebook cell
%matplotlib inline
# - interactive plots displayed in a notebook cell
# %matplotlib notebook (interactive version)

# Set matplotlib style
import matplotlib.pyplot as plt
plt.style.reload_library()
# print(plt.style.available) 
# combine styles (right overwrites left wherever they overlap):
plt.style.use(['default', 'plotea'])
# plt.style.use(['default'])

# Configure logging -------------------------------------------

# 1. Set up loggers, handlers and load the log_lvl function
from jupconfig.loggers import *

# 2. Set level of log-messages
log_lvl(ERROR) # you can also use lll() alias
# Other options in order of increasing importance and 
# decreasing verbosity:
# TRACE, DEBUG, INFO, WARNING, ERROR, CRITICAL
# or using integers: 0, 10, 20, 30, 40, 50, respectively

# Autocompleting ----------------------------------------------
# (not sure if that works)
#%config IPCompleter.greedy=True 

# Automatically reload modules before execution
%load_ext autoreload
%autoreload 2