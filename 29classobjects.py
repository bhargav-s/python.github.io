class Game:
    life = 3

    def Enemy(self):
        print('hit!!')
        self.life -= 1
    def Checklife(self):
        if self.life <= 0:
            print('dead')
        else:
            print(str(self.life) + ' ' + 'lives left')


enemy = Game()
enemy1 = Game()

enemy.Enemy()
enemy.Enemy()
enemy.Checklife()

enemy1.Enemy()
enemy1.Checklife()