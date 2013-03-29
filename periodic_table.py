from nucleus import *
import operator

def sumproduct(*lists):
  return sum(reduce(operator.mul, data) for data in zip(*lists))

#atomic number = protons
#ex. ag - 47, 60;62

#global atomic_mass, stable_with
class chemical_element:
  def __init__(self, name='', symbol='', category='', 
      protons_num=0, neutrons_num=[], atomic_mass=[],
      stable_with=[], stand_atomic_weight=1.0):

    self.name = name
    self.symbol = symbol
    self.category = category
    self.protons_num = protons_num
    self.neutrons_num = neutrons_num
    self.atomic_mass = atomic_mass
    self.stable_with = stable_with
    self.stand_atomic_weight = stand_atomic_weight

def relative_atomic_mass(atomic_mass, stable_with):
  sumproduct_rel_at_mass = sumproduct(atomic_mass, stable_with)
  print sumproduct_rel_at_mass

# list of few chemical elements for testing
Ag = chemical_element('Silver','Ag','transition metal',
    47, [60,62], [107, 109], [0.51839, 0.48161], 107.868)
P  = chemical_element('Phosphorus','P','nonmetal',
    15, [16], [31] ,[1.0], 30.973)
Rh = chemical_element('Rhodium','Rh','transition metal',
    45, [58], [103], [1.0], 102.905)
Pd = chemical_element('Palladium','Pd','transition metal',
    46, [56,58,59,60,62], [102,104,104,106,108],
    [0.0102,0.1114,0.2233,0.2733,0.2646], 106.42)
