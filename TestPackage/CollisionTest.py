import sys
import pygame
import os
pygame.init()

white = (255, 255, 255)

screenWidth = 960
screenHeight = 768
gameDisplay = pygame.display.set_mode([screenWidth, screenHeight])
pygame.display.set_caption("2D Game")
 
gameExit = False
 
clock = pygame.time.Clock()

with open("../Levels/ProjectEen.txt", "r") as f:
    imageLocation = f.read().splitlines()

level1Images = []
for image in imageLocation:
    level1Images.append(pygame.image.load("../" + image).convert_alpha())

x1 = 0
y1 = 0
x1Change = 0
y1Change = 0

x2 = 100
y2 = 100
x2Change = 0
y2Change = 0

playerChange = 0
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1Change -= 5
            if event.key == pygame.K_RIGHT:
                x1Change += 5
            if event.key == pygame.K_UP:
                y1Change -= 5
            if event.key == pygame.K_DOWN:
                y1Change += 5
            if event.key == pygame.K_a:
                x2Change -= 5
            if event.key == pygame.K_d:
                x2Change += 5
            if event.key == pygame.K_w:
                y2Change -= 5
            if event.key == pygame.K_s:
                y2Change += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x1Change = 0
            if event.key == pygame.K_RIGHT:
                x1Change = 0
            if  event.key == pygame.K_UP:
                y1Change = 0
            if event.key == pygame.K_DOWN:
                y1Change = 0
            if event.key == pygame.K_a:
                x2Change = 0
            if event.key == pygame.K_d:
                x2Change = 0
            if  event.key == pygame.K_w:
                y2Change = 0
            if event.key == pygame.K_s:
                y2Change = 0


    x1 += x1Change
    x2 += x2Change

    y1 += y1Change
    y2 += y2Change

    gameDisplay.fill(white)

    gameDisplay.blit(level1Images[1], (x1, y1))
    gameDisplay.blit(level1Images[1], (x2, y2))

    pygame.display.update()
    clock.tick(60)
 
pygame.quit()
