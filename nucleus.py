# Copyright 2013 defm03
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

import math

# prototypes -------------------- #
list_neutron = []
list_proton = []
nucleon_mass_u = 1.0
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

class charge:
  def __init__(self, chrg_type="", chrg_number=0):
    self.chrg_type = chrg_type
    self.chrg_number = chrg_number

    positive_charge = ""
    negative_charge = ""
    charged = 1
    non_charge = 0

    if chrg_type == "+":
      chrg_type_sym = positive_charge
    if chrg_type == "-":
      chrg_type_sym = negative_charge

    if chrg_num >= 1:
      chrg_type_num = charged

    if chrg_type == "0" and chrg_number == 0:
      chrg_type_num = non_charge

  def chrg_type(self, chrg_type_sym="", 
      chrg_type_num=0):
    self.chrg_type_sym = chrg_type_sym
    self.chrg_type_num = chrg_type_num

class proton:
  def __init__(self, mass, charge):
    self.mass = float(mass)
    self.charge = float(charge)
    self.list_proton = list_proton

    list_proton.append(mass)
    list_proton.append(charge)

class neutron:
  def __init__(self, mass, charge):
    global list_neutron
    self.mass = float(mass)
    self.charge = charge
    self.list_neutron = list_neutron

    list_neutron.append(mass)
    list_neutron.append(charge)

class nucleon:
  def __init__(self, proton, neutron):
    self.proton = proton
    self.neutron = neutron

  
  def rel_atomic_mass(self):
    pass

proton_charge = charge("+",1)
electron_charge = charge("-", 1)
neutron_charge = charge("0",0)

