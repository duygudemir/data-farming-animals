from farm.animal import Animal

class Chicken(Animal):
    def __init__(self, gender):
        # super() ile Animal sınıfından enerjiyi (energy=0) alıyoruz.
        super().__init__()
        self.gender = gender
        self.eggs = 0

    def talk(self):
        # Cinsiyete göre tavuğun çıkardığı ses değişiyor.
        if self.gender == "female":
            return "cluck cluck"
        else:
            return "cock-a-doodle-doo"

    def feed(self):
        # Önce ana sınıfın feed metodunu çağırıp enerjiyi 1 artırıyoruz.
        super().feed()
        # Eğer tavuk dişi ise 2 yumurta üretir, erkek ise 0 üretir.
        if self.gender == "female":
            self.eggs += 2
        else:
            self.eggs += 0