from oyuncu import Oyuncu
from silah import Silah
from dusman import Dusman

import random

print("RPG savaş sistemli prototip oyuna hoş geldiniz")

ad = input("adın nedir ")
düşman_seçimi = input("""hangi düşmanı istersin
zombi
dev
hayalet
""")
düşman_hasarı = random.randint(10, 15)
düşman = Dusman(düşman_seçimi, 100, 10, 15)
kilic = Silah("kılıç",10, 15)
mizrak = Silah("mızrak",15, 25)
yay = Silah("yay",12, 20)
silah_secimi = input("""bir silah seç
kılıç
mızrak
yay
""").lower( )

oyuncu1 = Oyuncu(ad, 100, kilic)

if silah_secimi == "kılıç":
	oyuncu1.silah_degistir(kilic)
elif silah_secimi == "mızrak":
	oyuncu1.silah_degistir(mizrak)
elif silah_secimi == "yay":
	oyuncu1.silah_degistir(yay)

while oyuncu1.can > 0 and düşman.can > 0:
	secim = input("""karşında bir düşman duruyor ne yapmak istersin
vur 
kaç 
""").lower( )
	if secim == "vur":
		oyuncu1.vur(düşman)
		if düşman.can > 0:
			düşman.vur(oyuncu1)
	elif secim == "kaç":
		print("görüşürüz")
		break
	else:
		print("kararınızı giriniz ")
		
if oyuncu1.can <= 0:
	print("kaybettin")
elif düşman.can <= 0:
	print("kazandın")