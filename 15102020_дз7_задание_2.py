
class Clothes:
    def __init__(self,type, parameter):
        self.type = type
        self.parameter = parameter
    @property
    def cloth_rate(self):
            if self.type == 'coat':
               return round(self.parameter / 6.5 + 0.5,2)
            elif self.type == 'suit':
                return round(self.parameter * 2 + 0.3,2)
            else:
                return 0 # вдруг неизвестный тип одежды

c1 = Clothes('coat', 48)
c2 = Clothes('suit', 1.76)
#c1 = Clothes('drysuit', 52)
print(c1.cloth_rate)
print(c2.cloth_rate)
print(c1.cloth_rate + c2.cloth_rate)