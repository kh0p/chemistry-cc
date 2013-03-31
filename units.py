# exact numbers 
# mensured numbers
# significant figures
float = 0.0
import math
class unit_type:
  def __init__(self, name='', symbol='', val=1.0):
    self.name = name
    self.symbol = symbol
    self.val = val
  def unit_pow(self, power=1):
    #km^2, km^3 etc.
    self.power = power
    if power == 2:
      self.val * pow(10,2)
    elif power == 3:
      self.val * pow(10,3)
    else:
      pass
km = unit_type('Kilometre', 'km', 1.0)
m = unit_type('Metre', 'm', 1.0)
km_to_m = m.val * pow(10,3)
#km.val = m.val * pow(10,3)
g = unit_type('Gram', 'g', 1.0)
#to count >> atoms in 12grams of C-12
#1 mole
mole_C_12 = 6.022 * pow(10,23) #12grams
mole_O    = 6.022 * pow(10,23) #16grams // O amu=16
#  MOLAR MASS (M) in gram = RELATIVE ATOMIC MASS (RAM) in amu
u = unit_type('units', 'u', 1.66*pow(10,-27)) # val in kg

