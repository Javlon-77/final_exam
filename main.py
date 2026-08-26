class Transport:

  def init(self, nomi, tezlik):
    self.nomi = nomi
    self.tezlik = tezlik

  def harakat(self):
    print("Transport harakatlanmoqda!!!")


class Avtomobil(Transport):

  def harakat(self):
    print(f"Avtomobil yolda yuryapti Tezligi: {self.tezlik} km/soat")

class velosiped(Transport):

  def harakat(self):
    print(f"Velosiped pedal bosmoqda Tezligi...: {self.tezlik} km/soat")


auto = Avtomobil("nexia", 100)
velo = velosiped("morgan", 20)

auto.harakat()
velo.harakat()
