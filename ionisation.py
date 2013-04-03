from nucleus import *
from stechiometry import *
from molecule import *
# X(g) --->  x+(g) + e-
# '+' and '-' after 'x' and 'e' is charge
# Ionisation energy: First ionisation en-
# ergy is required to remove the most lo-
# osely held electron fron one mole of g-
# aseous atoms to produce 1 mole of gase-
# ous ions each with charge of 1+.
# including: moles

class fromtoIonisation:
  def __init__(self, molecule, electron_num):
    global products
    products = []
    self.molecule = molecule
    self.electron_num = electron_num
    molecule == Molecule.chem_el_xx + electron_num

