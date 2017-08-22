"""
Four-momentum vector class
Adapted from
    https://github.com/ibab/missing_hep.git

The FourMomentum is a total momentum of a single isolated syste.  IT is best  
represented by
        P.E[i]   P.px[i]    P.py[i]    P.pz[i]
      __                               __
Pt =  | Ea,     Pxa,      Pya,      Pza |   {i 1}
      | Eb,     Pxb,      Pyb,      Pzb |   {i 2}
      ...
"""
import numpy as np

# General FourMomentum class with P = array(E[], px[], py[], pz[])
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

  def __sub__(self, other):
    return FourMomentum(
      self.E - other.E,
      self.px - other.px,
      self.py - other.py,
      self.pz - other.pz
    )

  # def __mul__(self, other):
    # q, r = np.linalg.qr(self)
    # return q, r
    
  def mass(self):
    return np.sqrt(np.square(self.E) - np.square(self.px))

# for i, element in enumerate(P.E):
    # E_value = element
    # print(i, E_value)