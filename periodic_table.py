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

  def relative_atomic_mass(self, atomic_mass, stable_with):
    sumproduct(atomic_mass, stable_with)

# list of few chemical elements for testing
Ag = chemical_element('Silver','Ag','transition metal',
    47, [60,62], [107, 109], [0.51839, 0.48161], 107.868)
P  = chemical_element('Phosphorus','P','nonmetal',
    15, [16], [31] ,[1.0], 30.973)
