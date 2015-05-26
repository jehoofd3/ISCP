#!/usr/bin/env python

from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

x = 0.0
y = 0.0


class Texture():
    # simple texture class
    # designed for 32 bit png images (with alpha channel)
    def __init__(self, fileName):
        self.texID = 0
        self.LoadTexture(fileName)

    def LoadTexture(self, fileName):
        try:
            textureSurface = pygame.image.load(fileName)
            textureData = pygame.image.tostring(textureSurface, "RGBA", 1)


            self.texID = glGenTextures(1)

            glBindTexture(GL_TEXTURE_2D, self.texID)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, textureSurface.get_width(), textureSurface.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        except:
            print "can't open the texture: %s" % (fileName)

    def __del__(self):
        glDeleteTextures(self.texID)


class Main():
    def resize(self, (width, height)):
        if height == 0:
            height = 1

        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)

        glLoadIdentity()
        gluOrtho2D(0, 640, 480, 0, -1, 1)
        glMatrixMode(GL_MODELVIEW)

    def init(self):
        # set some basic OpenGL settings and control variables
        glShadeModel(GL_SMOOTH)
        glEnable(GL_BLEND)

        self.tutorial_texture = Texture("PixelTree.png")

        self.demandedFps = 30.0
        self.done = False

    def draw(self, ix, iy, width, height):
        globals()["x"] = ix
        globals()["y"] = iy

        glEnable(GL_TEXTURE_2D)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        glTranslatef(x, y, 0.0)

        glBindTexture(GL_TEXTURE_2D, self.tutorial_texture.texID)

        glBegin(GL_QUADS)

        glTexCoord2f(0, 0)
        glVertex2f(0, 0)

        glTexCoord2f(0, 1)
        glVertex2f(0, height)

        glTexCoord2f(1, 1)
        glVertex2f(width, height)

        glTexCoord2f(1, 0)
        glVertex2f(width, 0)

        glEnd()
        glLoadIdentity()



    def Input(self):
        mpb = pygame.mouse.get_pressed()  # mouse pressed buttons
        kpb = pygame.key.get_pressed()  # keyboard pressed buttons
        msh = pygame.mouse.get_rel()  # mouse shift

        if kpb[K_ESCAPE]:
            self.done = True

        if kpb[K_UP]:
            globals()["y"] += 1

        if kpb[K_DOWN]:
            globals()["y"] -= 1

        if kpb[K_RIGHT]:
            globals()["x"] += 1

        if kpb[K_LEFT]:
            globals()["x"] -= 1


    def __init__(self):

        video_flags = OPENGL | DOUBLEBUF

        pygame.init()
        pygame.display.set_mode((640, 480), video_flags)

        pygame.display.set_caption("www.jason.gd")

        self.resize((640, 480))
        self.init()

        clock = pygame.time.Clock()
        while 1:
            glClear(GL_COLOR_BUFFER_BIT)
            event = pygame.event.poll()
            if event.type == QUIT or self.done:
                pygame.quit()
                break

            self.Input()
            self.draw(x, y, 64, 64)

            pygame.display.flip()

            # limit fps
            clock.tick(self.demandedFps)

            print "X: " , x
            print "Y: ",  y
            print


if __name__ == '__main__': Main()