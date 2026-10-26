import unittest
from farm.cow import Cow

class TestCow(unittest.TestCase):
    
    def setUp(self):
        # Her testten önce yeni bir inek nesnesi oluşturuyoruz
        self.cow = Cow()

    def test_initialize_sets_milk_to_zero(self):
        # İnek ilk doğduğunda süt miktarı 0 olmalı
        self.assertEqual(self.cow.milk, 0)

    def test_initialize_sets_energy_to_zero(self):
        # İnek ilk doğduğunda enerjisi 0 olmalı
        self.assertEqual(self.cow.energy, 0)

    def test_feed_extends_method(self):
        # Beslendiğinde hem enerji artmalı hem de süt üretilmeli (metodun genişletildiğini test ediyoruz)
        self.cow.feed()
        self.assertEqual(self.cow.energy, 1)

    def test_feed_adds_milk(self):
        # Beslendiğinde süt miktarı 2 litre artmalı
        self.cow.feed()
        self.assertEqual(self.cow.milk, 2)

    def test_feed_adds_energy(self):
        # Beslenme sonucunda enerjinin doğru arttığını doğruluyoruz
        initial_energy = self.cow.energy
        self.cow.feed()
        self.assertEqual(self.cow.energy, initial_energy + 1)

    def test_talk_returns_moo(self):
        # İnek konuştuğunda "moo" sesini vermeli
        self.assertEqual(self.cow.talk(), "moo")