from collections import namedtuple

Fermion = namedtuple("Fermion", ["mass_singlet", "mass_doublet", "y1", "y2"])

if __name__ == "__main__":
    fermion = Fermion(0.0, 0.1, 0.2, 0.3)
    print(fermion)
