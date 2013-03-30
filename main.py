# Copyright 2013 defm03
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

from nucleus import *
from periodic_table import *
from density import *
from units import *
def main():
  # tests
  a = neutron(neutron_mass_u, neutron_eC_charge)
  b = proton(proton_mass_u, proton_eC_charge)

  print a
  print b
  print ""
  print str(a.charge)
  print str(b.charge)

  get_info_test = get_info(40.5,15.0)
  density_count = density(get_info_test.mass, get_info_test.Volume)

  print density_count

  Ag_relative_mass = relative_atomic_mass(Ag.atomic_mass, Ag.stable_with)

  print str(km.val) + "km = " + str(km_to_m) + "m"

if __name__ == '__main__':
  main()
