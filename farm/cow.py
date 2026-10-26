from farm.animal import Animal

class Cow(Animal):
    def __init__(self):
        # super() diyerek ana sınıfımız olan Animal'ın __init__ metodunu çalıştırıyoruz.
        # Böylece ineğin de başlangıç enerjisi 0 oluyor.
        super().__init__()
        self.milk = 0

    def talk(self):
        # İneğin çıkardığı karakteristik ses
        return "moo"

    def feed(self):
        # Önce ana sınıfın (Animal) feed metodunu çalıştırıp enerjiyi 1 artırıyoruz.
        super().feed()
        # Ek olarak inek beslendiğinde 2 litre süt üretir.
        self.milk += 2