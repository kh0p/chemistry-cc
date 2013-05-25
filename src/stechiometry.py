# amu = 1/12 mass of an atom of carbon-12
from nucleus import *
from units import *
#6.022 * pow(10,23) <- avogadro's number/chem constant
avogadro_const = 6.022 * pow(10,23)
#it's also number of atoms in 12 grams of carbon-12
def to_Moles(name='',relative_atomic_mass=0.0):
  #when we get relative_atomic_mass from periodic_table
  #in -> amu to -> moles
  chemical_element.name = name
  #each element mole = 6.022 * pow(10,23)
  #took me a while to realize @__@

  print str(name) + " " + str(relative_atomic_mass)
mole = 0
g/mole*pow(1,-1) == u
# [g * mole * pow(1,-1)]
