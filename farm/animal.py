class Animal:
    def __init__(self):
        # Her hayvan doğduğunda başlangıç enerjisi 0 olarak başlar.
        self.energy = 0

    def feed(self):
        # Hayvan beslendiğinde enerjisi 1 artar.
        self.energy += 1