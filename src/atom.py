from nucleus import *
from orbitals import *
from periodic_table import *
down_indx = 0
class atom:
  def __init__(self, nucleus=[0,0],electrons=0):
    #nucleus[0] == protons
    #nucleus[1] == neutrons
    self.nucleus = nucleus
    self.electrons = electrons
    
    self.electrons == self.nucleus[0]
  def chem_el_x(self, name="",num_of_atoms=0):
    self.num_of_atoms = num_of_atoms
    self.name = name
    name == chemical_element.name
    num_of_atoms == down_indx
