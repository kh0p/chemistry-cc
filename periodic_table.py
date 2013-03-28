from nucleus import *

#atomic number = protons
#ex. ag - 47, 60;62

class chemical_element:
  def __init__(self, name="", symbol="", category="", 
      atomic_weight=0, protons_num=0, neutrons_num=[],
      stable_with=[]):

    self.name = name
    self.symbol = symbol
    self.category = category
    self.atomic_weight = atomic_weight
    self.protons_num = protons_num
    self.neutrons_num = neutrons_num
    self.stable_with = stable_with

    neutrons_combinations = len(stable_with)

  def relative_atomic_mass(self): 
    pass

# list of few chemical elements for testing
Ag = chemical_element('Silver','Ag','transition metal',
    107.868, 47, [60,62])
P  = chemical_element('Phosphorus','P','nonmetal',
    30.973, 15, [16])


