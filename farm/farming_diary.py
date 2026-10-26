"""
Bu komut dosyası, hayvanların etkileşime girip eylemler gerçekleştirdiği bir çiftlik günlüğünü simüle eder.
"""

from farm.cow import Cow
from farm.chicken import Chicken

print("\n\n📝 Day Three: Animals Talk")

# Hayvan nesnelerimizi oluşturuyoruz
cow = Cow()
female_chicken = Chicken('female')
male_chicken = Chicken('male')

# Hayvanları konuşturuyoruz
print(f"The cow says {cow.talk()}")
print(f"The female chicken says {female_chicken.talk()}")
print(f"The male chicken says {male_chicken.talk()}")

print("\n\n📝 Day Four: Feed The Animals")

# 1. Tüm hayvanları `animals` listesinde saklıyoruz
animals = [cow, female_chicken, male_chicken]

# 2. Döngü kullanarak her hayvan için `feed` metodunu çağırıyoruz
for animal in animals:
    animal.feed()

# 3. Üretilen miktarları ekrana yazdırıyoruz
print(f"The cow produced {cow.milk} liters of milk")
print(f"The female chicken produced {female_chicken.eggs} eggs")
print(f"The male chicken produced {male_chicken.eggs} eggs")