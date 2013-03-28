from nucleus import *
import operator

def sumproduct(*lists):
  return sum(reduce(operator.mul, data) for data in zip(*lists))

#atomic number = protons
#ex. ag - 47, 60;62

#global atomic_mass, stable_with
atomic_mass = []
stable_with = []
class chemical_element:
  def __init__(self, name='', symbol='', category='', 
      atomic_weight=0, protons_num=0, neutrons_num=[],
      atomic_mass_=[], stable_with_=[], stand_atomic_weight=1.0):

    atomic_mass_ = atomic_mass
    stable_with_ = stable_with

    self.name = name
    self.symbol = symbol
    self.category = category
    self.atomic_weight = atomic_weight
    self.protons_num = protons_num
    self.neutrons_num = neutrons_num
    self_atomic_mass = atomic_mass
    self.stable_with = stable_with
    self.stand_atomic_weight = stand_atomic_weight

  def relative_atomic_mass(self, mass=[], perc=[]):
    self.mass = mass
    self.perc = perc

    sumproduct(mass, perc)

# list of few chemical elements for testing
Ag = chemical_element('Silver','Ag','transition metal',
    107.868, 47, [60,62], [107, 109], [0.51839, 0.48161], 107.868)
P  = chemical_element('Phosphorus','P','nonmetal',
    30.973, 15, [16], [31] ,[1.0], 30.973)
