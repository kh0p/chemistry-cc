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
      stable_with=[], stand_atomic_weight=1.0,
      period=0,group=0):

    self.name = name
    self.symbol = symbol
    self.category = category
    self.protons_num = protons_num
    self.neutrons_num = neutrons_num
    self.atomic_mass = atomic_mass
    self.stable_with = stable_with
    self.stand_atomic_weight = stand_atomic_weight
    self.period = period
    self.group = group
    
def relative_atomic_mass(atomic_mass, stable_with):
  sumproduct_rel_at_mass = sumproduct(atomic_mass, stable_with)
  print sumproduct_rel_at_mass

# list of few chemical elements for testing
H  = chemical_element('Hydrogen', 'H', 'nonmetal',
    1, [0,1], [1, 2], [0.99985,0.00015], 1.008, 1, 1)
Ag = chemical_element('Silver','Ag','transition metal',
    47, [60,62], [107, 109], [0.51839, 0.48161], 
    107.868, 6, 11)
P  = chemical_element('Phosphorus','P','nonmetal',
    15, [16], [31] ,[1.0], 30.973, 3, 15)
Rh = chemical_element('Rhodium','Rh','transition metal',
    45, [58], [103], [1.0], 102.905, 5, 9)
Pd = chemical_element('Palladium','Pd','transition metal',
    46, [56,58,59,60,62], [102,104,104,106,108],
    [0.0102,0.1114,0.2233,0.2733,0.2646], 106.42, 5, 10)
Cd = chemical_element('Cadmium','Cd','transition metal',
    48, [62,63,64],[110,111,112], [0.1249,0.128,0.2413],
    112.411, 5, 12)
In = chemical_element('Indium','In','post-transition metal',
    49, [64], [113], [0.043], 114.818, 5, 13)
