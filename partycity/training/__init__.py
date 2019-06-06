"""
Python package for training the PartyCity algorithm.
----------------------------------------------------
This is where we specify all outward facing functions, i.e.
functions that may be called by our main.py in the partycity
package root folder.

Brian Sutherland <bsuth@umich.edu>
Shameek Ray <shameek@umich.edu>
Nikita Badhwar <nbadhwar@umich.edu>
"""

import os
TRAINING_DIR = os.path.dirname(__file__)

from partycity.training.preprocess import gen_training_data
from partycity.training.train import train_nb
from partycity.training.train import train_rocchio
from partycity.training.train import train_text_blob
