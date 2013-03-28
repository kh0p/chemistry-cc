#!bin/zsh

import math

# prototypes -------------------- #
x = 0
# ------------------------------- #

proton_symb   = ["p","p+","N+"] # temp. - I'm gonna change '+', '0'
neutron_symb  = ["n","n0","N0"] # etc. to upindex soon propably by
electron_symb = ["e-","beta-"]  # putchar method in python lib -sys

#const values for proton
proton_mass_kg = 1.672621 * pow(10,-27) #kg
proton_mass_u = 1.007276 #atomic mass unit
proton_e_charge = "+1" # e = elementary charge
proton_eC_charge = 1.602176 * pow(10,-19) #C
#const values for neutron
neutron_mass_kg = 1.674927 * pow(10,-27) #kg
neutron_mass_u = 1.008664 #atomic mass unit
neutron_e_charge = "0e" # e = elementary charge
neutron_eC_charge = 0 #C
#const values for electron
electron_mass_kg = 9.109382 * pow(10,-31) #kg
electron_mass_u1 = 5.485799 * pow(10,-4) #u
electron_e_charge = "-1" # e = elementary charge
electron_eC_charge = -1.602176 * pow(10,-19)

def proton(self, mass=1.0, charge=1.0):
  global proton_val_list
  self.mass = mass
  self.charge = charge

  proton_val_list = []
  proton_val_list.append(mass)
  proton_val_list.append(charge)

def neutron(self, mass=1.0, charge=1.0):
  global neutron_val_list
  self.mass = mass
  self.charge = charge

  neutron_val_list = []
  neutron_val_list.append(mass)
  neutron_val_list.append(charge)

class nucleon:
  def __init__(self):
    int(proton_val_list[0]) + int(neutron_val_list[0]) == nucleon_mass_u
  
  def rel_atomic_mass(self):
    pass

def main():
  neutron(neutron_mass_u, neutron_eC_charge)
  proton(proton_mass_u, neutron_eC_charge)
  randomnucleon.nucleon()
  print proton
  print neutron
  print nucleon_mass_u

if __name__ == '__main__':
  main()

