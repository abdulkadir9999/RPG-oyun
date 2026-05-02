import random

class Oyuncu:
	def __init__(self, isim, can, silah):
		self.isim = isim
		self.can = can
		self.silah = silah
	
	def vur(self, dusman):
	   hasar = random.randint(self.silah.min_hasar, self.silah.max_hasar)
	   dusman.can -= hasar
	   print(self.isim, "düşmana", hasar, "vurdu")
	   print("Düşman canı:", dusman.can)

	def silah_degistir(self, yeni_silah):
	   self.silah = yeni_silah
	   print(self.isim, "artık", yeni_silah.isim, "kullanıyor!")