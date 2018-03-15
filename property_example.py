class Ising:
    def __init__(self):
        self._beta = None
        self._T = None

    @property
    def beta(self):
        return self._beta

    @beta.setter
    def beta(self, beta):
        self._beta = beta
        self._T = 1/beta

    @property
    def T(self):
        return self._T

    @T.setter
    def T(self, T):
        self._beta = 1/T
        self._T = T


if __name__ == "__main__":
    ising = Ising()
    ising.beta = 100
    print(ising.T)
