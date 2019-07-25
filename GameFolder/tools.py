class Tore:

    def __init__(self, limit, val = 0):
        self.val= val
        self.limit = limit

    def __add__(self,st):
        return (self.val + st)%self.limit

    def __sub__(self,st):
        return (self.val - st)%self.limit

    def __str__(self):
        return str(self.val)

    def __int__(self):
        return self.val


class snakeBody:

    def __init__(self, limitX,limitY):
        self.body = []
        self.limitX= limitX
        self.limitY = limitY

    def add(self,x,y):
        self.body.append( [Tore(self.limitX,x),Tore(self.limitY,y)])

    def move(self,action):
        if(action == "up"):
            mv = [0,-1]
        if(action == "down"):
            mv = [0,1]
        if(action == "left"):
            mv = [-1,0]
        if(action == "right"):
            mv = [1,0]
        else:
            mv = [0,0]
