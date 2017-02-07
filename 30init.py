class Enemy:
    def __init__(self,x):
        self.energylevel = x

    def levelvalue(self):
        print(self.energylevel)

bhargav = Enemy(5)

bhargav.levelvalue()