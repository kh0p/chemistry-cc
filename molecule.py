from atom import *
atom_list = {}
class Molecule:
  def __init__(self, chem_el_x, full_molecule = ""):
    self.atom_list = atom_list
    self.full_molecule = full_molecule
    atom_list[chem_el_x.name] = chem_el_x.num_of_atoms

H_molecule = atom([1,0],1)
H_molecule.chem_el_x(H,2)
H_molecule_out = Molecule()

