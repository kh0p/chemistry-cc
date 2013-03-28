# Copyright 2013 defm03
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

from nucleus import *

def main():
  # tests
  a = neutron(neutron_mass_u, neutron_eC_charge)
  b = proton(proton_mass_u, proton_eC_charge)
  c = nucleon()
  print a
  print b
  print c
  print ""
  print str(a.charge)
  print str(b.charge)

if __name__ == '__main__':
  main()
