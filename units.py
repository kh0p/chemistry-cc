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
  def unit_pow(self, power):
    #km^2, km^3 etc.
    pass
km = unit_type('Kilometre', 'km', 1.0)
m = unit_type('metre', 'm', 1.0)
km_to_m = m.val * pow(10,3)
#km.val = m.val * pow(10,3)

