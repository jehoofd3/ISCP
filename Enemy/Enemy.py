from Helpers.Artist import *

class Enemy():

    width = 0
    height = 0
    x = 0
    y = 0
    xSpeed = 0
    ySpeed = 0
    texturePath = "Test.png"

    def __init__(self, width, height,x , y, texturePath):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.texturePath = texturePath


    def update(self):
        self.x += self.xSpeed
        self.y -= self.ySpeed


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.xSpeed -= 5
                if event.key == pygame.K_RIGHT:
                    self.xSpeed += 5
                    print self.x
                if event.key == pygame.K_UP:
                    self.jump()

    def draw(self):
        drawTextures(self.texturePath, self.x, self.y, self.width, self.height)
        print self.width
        print self.height
        print

    def jump(self):
        self.ySpeed += 10