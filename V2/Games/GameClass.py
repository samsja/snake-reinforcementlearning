

class Game:
    def __init__(self,NbInput):
        self.NbInput = NbInput

    def move(self,action):
        if( not(isinstance(action,int))):
            raise Exception('argument errors','the action ' + str(action) + " is not an integer")

        elif( action <0 or action >= self.NbInput):
            raise Exception('argument errors','the action ' + str(action) + " is not between 0 and " + str(self.NbInput -1 ))

    def getInputs(self):
        return [i for i in range(self.NbInput)]


a = Game(3)

a.move(1)

print(a.getInputs())
