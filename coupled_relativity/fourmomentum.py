"""
Four-momentum vector class
Adapted from
    https://github.com/ibab/missing_hep.git
"""

import numpy as np

class FourMomentum:

  def __init__(self, E, px, py, pz):
    self.E = np.array(E)
    self.px = np.array(px)
    self.py = np.array(py)
    self.pz = np.array(pz)

  def __add__(self, other):
    return FourMomentum(
             self.E + other.E,
             self.px + other.px,
             self.py + other.py,
             self.pz + other.pz
           )
    
  def mass(self):
    return np.sqrt(self * self)
