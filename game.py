import pygame

from neuralnetwork import NeuralNetwork


class Bar:
    def __init__(self):
        self.length = 120
        self.height = 16
        self.bar_x = (Game.width-self.length)/2
        self.bar_y = Game.height-self.height
        self.center_x = (Game.width/2)
        self.center_y = Game.height-(self.height/2)
        self.radius = 15
        self.ball_x = self.center_x
        self.ball_y = self.bar_x+(self.length)/2-(2*self.radius)
        self.ball_center_x = 100
        self.ball_center_y = 100
        self.ball_vel_x = 10
        self.ball_vel_y = 10
        self.bar_vel = 0
    def showBar(self,x,y):
        pygame.draw.rect(Game.gameDisplay,Game.black,[x,y,self.length,self.height])

    def showBall(self,x,y):
        pygame.draw.circle(Game.gameDisplay,Game.gray,(int(x),int(y)),self.radius)


class Game():
    width = 800
    height = 600
    black = (0,0,0)
    gray = (70,70,70)
    gameDisplay = pygame.display.set_mode((width, height))

    def __init__(self):

        pygame.init()
        self.clock = pygame.time.Clock()
        self.bar = Bar()
        self.gameLoop()

    def gameLoop(self):
        gameExit = False
        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
            keys = pygame.key.get_pressed()
            self.bar.ball_center_x += self.bar.ball_vel_x
            self.bar.ball_center_y += self.bar.ball_vel_y
            if (self.bar.ball_center_y+self.bar.radius)>= (Game.height-self.bar.height):
                if self.bar.ball_center_x >= self.bar.bar_x and self.bar.ball_center_x <=(self.bar.bar_x+self.bar.length):
                    self.bar.ball_vel_y = -self.bar.ball_vel_y
            if self.bar.ball_center_x >= Game.width or self.bar.ball_center_x-self.bar.radius<=0:
                self.bar.ball_vel_x = -self.bar.ball_vel_x

            if self.bar.ball_center_y<=0:
                self.bar.ball_vel_y = -self.bar.ball_vel_y
            if self.bar.ball_center_y > Game.height:
                gameExit = True

            if keys[pygame.K_LEFT]:
                if self.bar.bar_x!=0:
                    self.bar.bar_x -= 10
                    self.bar.center_x -=10
            if keys[pygame.K_RIGHT]:
                if self.bar.bar_x!=(Game.width-self.bar.length):
                    self.bar.bar_x += 10
                    self.bar.center_x += 10
            self.bar.showBar(self.bar.bar_x,self.bar.bar_y)
            self.bar.showBall(self.bar.ball_center_x,self.bar.ball_center_y)
            pygame.display.update()
            self.gameDisplay.fill((135,206,250))
            self.clock.tick(30)
        pygame.quit()
        quit()

if __name__ == '__main__':
    game = Game()