class plantae:
    def intro(self):
        print("Plantae adalah makhluk hidup eukariotik yang memiliki dinding sel")

    def deskripsi(self):
        print("Plantae termasuk makhluk hidup yang dapat melakukan fotosintesis")

class monokotil(plantae):
    def deskripsi(self):
        print("Monokotil adalah subclass dari plantae yang memiliki keping biji satu")

class dikotil(plantae):
    def deskripsi(self):
        print("Dikotil adalah subclass dari plantae yang memiliki keping biji dua")

obj_plantae = plantae()
obj_monokotil = monokotil()
obj_dikotil = dikotil() 

obj_plantae.intro()
obj_plantae.deskripsi()

obj_monokotil.intro()
obj_monokotil.deskripsi()

obj_dikotil.intro()
obj_dikotil.deskripsi()