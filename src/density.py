# rho = m/V
# density = mass/Volume
# kg/m^3 (SI) = kg/m^3

# electron density maybe?
# can be useful for orbitals

class get_info:
  def __init__(self, mass=0.1, Volume=0.1):
    self.mass = mass
    self.Volume = Volume
    
def density(mass, Volume):
  density_float = 0.1
  density_float = mass / Volume

  print density_float
