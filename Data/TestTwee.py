#!/usr/bin/env python

from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

class Texture():
# simple texture class
# designed for 32 bit png images (with alpha channel)
	def __init__(self,fileName):
		self.texID=0
		self.LoadTexture(fileName)
	def LoadTexture(self,fileName): 
		try:
			textureSurface = pygame.image.load(fileName)
			textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
			
			self.texID=glGenTextures(1)
			
			glBindTexture(GL_TEXTURE_2D, self.texID)
			glTexImage2D( GL_TEXTURE_2D, 0, GL_RGBA,
						textureSurface.get_width(), textureSurface.get_height(),
						0, GL_RGBA, GL_UNSIGNED_BYTE, textureData )
			glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
			glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
		except:
			print "can't open the texture: %s"%(fileName)
	def __del__(self):
		glDeleteTextures(self.texID)

class Main():
	def resize(self,(width, height)):
		if height==0:
			height=1
		glViewport(0, 0, width, height)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluOrtho2D(-8.0, 8.0, -6.0, 6.0)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

	def init(self):
		#set some basic OpenGL settings and control variables
		glShadeModel(GL_SMOOTH)
		glClearColor(0.0, 0.0, 0.0, 0.0)
		glClearDepth(1.0)
		glDisable(GL_DEPTH_TEST)
		glDisable(GL_LIGHTING)
		glDepthFunc(GL_LEQUAL)
		glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
		glEnable(GL_BLEND)
		
		self.tutorial_texture=Texture("PixelTree.png")
		
		self.demandedFps=30.0
		self.done=False
		
		self.x,self.y=0.0 , 0.0

	def draw(self):
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()
		glDisable(GL_LIGHTING)
		glEnable(GL_TEXTURE_2D)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		
		glPushMatrix()
		
		glTranslatef(self.x, self.y, 0.0)

		glColor4f(1.0, 1.0, 1.0,1.0)
		
		glBindTexture(GL_TEXTURE_2D,self.tutorial_texture.texID)
		
		glBegin(GL_QUADS)
		
		glTexCoord2f(0.0,1.0)
		glVertex2f(-1.0, 4.0)
		
		glTexCoord2f(1.0,1.0)
		glVertex2f(1.0, 4.0)
		
		glTexCoord2f(1.0,0.0)
		glVertex2f(1.0, -4.0)
		
		glTexCoord2f(0.0,0.0)
		glVertex2f(-1.0, -4.0)
		
		glEnd()
		
		glPopMatrix()
		
	def Input(self):
		mpb=pygame.mouse.get_pressed() # mouse pressed buttons
		kpb=pygame.key.get_pressed() # keyboard pressed buttons
		msh=pygame.mouse.get_rel() # mouse shift
		
		if kpb[K_ESCAPE]:
			self.done=True
			
		if kpb[K_UP]:
			self.y+=0.1
		if kpb[K_DOWN]:
			self.y-=0.1
		
		if kpb[K_RIGHT]:
			self.x+=0.1
		if kpb[K_LEFT]:
			self.x-=0.1
		
			
	def __init__(self):

		video_flags = OPENGL|DOUBLEBUF
		
		pygame.init()
		pygame.display.set_mode((640,480), video_flags)
		
		pygame.display.set_caption("www.jason.gd")
		
		self.resize((640,480))
		self.init()

		
		clock = pygame.time.Clock()
		while 1:
			event = pygame.event.poll()
			if event.type == QUIT or self.done:
				pygame.quit () 
				break
			
			self.Input()
			self.draw()
			
			pygame.display.flip()
			
			#limit fps
			clock.tick(self.demandedFps)

if __name__ == '__main__': Main()