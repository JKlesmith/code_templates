#!/usr/bin/env python3
#
# <Title>
# Author: Justin R. Klesmith
# Copyright (C) 2019 by Justin R. Klesmith
#

"""package - description"""

# python std lib imports 
from sys import version_info, exit

# python version check
if version_info < (3,6):
    exit("[Error] Your Python version is too old.\n"
          "Minimium version required is Python 3.6 - 64 bit.")

from os.path import isfile
from pathlib import Path 
    
# library import
try:
    import numpy as np
except ImportError:
    exit("[Error] Numpy is not installed and is required.")

try:
    import scipy as sp
except ImportError:
    exit("[Error] SciPy not installed and is required.")
    
try:
    import pandas as pd
except ImportError:
    exit("[Error] pandas not installed and is required.")
    
try:
    import sklearn as skl
except ImportError:
    exit("[Error] SciKit-Learn not installed and is required.")

try:
    import matplotlib.pyplot as plt
except ImportError:
    exit("[Error] matplotlib not installed and is required.")
    
try:
    import seaborn as sns
    sns.set(rc={'figure.figsize':(6,6),
                'axes.facecolor':'white',
                'figure.facecolor':'white'
                })
except ImportError:
    exit("[Error] Seaborn not installed and is required.")

# set the author information
__author__ = "Justin R. Klesmith"
__copyright__ = "Copyright 2019 - Justin R. Klesmith"
__license__ = "GPL-3"
__version__ = "20XX.X"
__maintainer__ = "Justin R. Klesmith"
__email__ = ""

# set file constants
file_path = str(Path().absolute().as_posix()) + '/'

"""
Import the data
"""
# set our filename
import_features = 'features.csv'

# read in our pact file    
if isfile(file_path + '/' + import_features):
        
    # load the csv of features into pandas
    df_dataset = pd.read_csv(file_path + '/' + import_features)

