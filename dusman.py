import random

class Dusman:
    def __init__(self, isim, can, min_hasar, max_hasar):
        self.isim = isim
        self.can = can
        self.min_hasar = min_hasar
        self.max_hasar = max_hasar

    def vur(self, oyuncu):
        hasar = random.randint(self.min_hasar, self.max_hasar)
        oyuncu.can -= hasar
        print("Düşman sana", hasar, "vurdu")
        print("Canın:", oyuncu.can)