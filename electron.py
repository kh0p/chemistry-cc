from nucleus import *
list_electron=[]
class electron:
  def __init__(self, mass, charge):
    self.mass = float(mass)
    self.charge = float(charge)
    self.list_electron = list_electron

    list_electron.append(mass)
    list_electron.append(charge)
