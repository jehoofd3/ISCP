import pygame


class PlayerAnimation():

    def __init__(self, player):
        # Deze class krijgt een object enemy mee. Het is mogelijk de afbeeldingen in de
        # constructor toe te voegen, maar dit lijkt me overbodig omdat je de lijsten
        # uit de enemy kan halen
        self.player = player
        self.walk_l = self.player.walk_l
        self.walk_r = self.player.walk_r
        self.dead_l = self.player.dead_l
        self.dead_r = self.player.dead_r
        self.jump_l = self.player.jump_l
        self.jump_r = self.player.jump_r

        # texture is de afbeelding. Er moet een default afbeelding mee gegeven worden anders is
        # de var in het eerste frame leeg. Hierdoor krijg je een error
        self.texture = pygame.image.load("../Data/Images/Enemy/Fly/l_0.png").convert_alpha()

        # frame_cap zijn de max beelden (frames) die elke seconde berekend worden
        # In de Boot class zetten we het op max 60
        self.frame_cap = 60

        # Deze var kijkt om de hoeveel frames er een afbeelding gewisseld moet worden.
        # We hebben er voor gekozen alle afbeeldingen in 1 sec (60 frames) te wisselen,
        # dit omdat het gebruikelijk is. Veel game engines doen het ook op deze manier.
        # frame_cap is 60, dit wordt gedeeld door de lengte van de list walk_l, hier
        # zitten 2 afbeeldingen in. Hierdoor wordt er om de 30 frames (0,5 seconde)
        # een andere afbeelding aan de enemy mee gegeven.
        self.tex_switch = self.frame_cap / len(self.walk_l)

        # De var frame_count is nodig om bij te houden hoeveel frames er verlopen zijn.
        # Dit is nodig om de afbeelding te wisselen
        self.frame_count = 0

        # Deze twee vars zijn nodig om bij te houden of de enemy naar links of rechts
        # loopt. Zo is het bij te houden welke dead image er terug gestuurd moet worden
        self.left_released = None
        self.right_released = None

        self.length_list = len(self.walk_l)


    def update(self):
        if(self.player.xSpeed > 0):
            self.right_walk()
            self.left_released = False
            self.right_released = True

        elif(self.player.xSpeed < 0):
            self.left_walk()
            self.left_released = True
            self.right_released = False

        elif(self.player.xSpeed == 0 and self.right_released):
            self.right_stand()

        elif(self.player.xSpeed == 0 and self.left_released):
            self.left_stand()

        if(self.player.ySpeed != 0 and self.right_released):
            self.right_jump()
        elif(self.player.ySpeed != 0 and self.left_released):
            self.left_jump()

        return self.texture

    def right_walk(self):
        if(self.frame_count >= self.frame_cap):
            self.frame_count = 0

        for i in range(self.length_list):
            if(self.frame_count / self.tex_switch == i):
                self.texture = self.walk_r[i]

        self.frame_count += 1

    def left_walk(self):
        if(self.frame_count >= self.frame_cap):
            self.frame_count = 0

        for i in range(self.length_list):
            if(self.frame_count / self.tex_switch == i):
                self.texture = self.walk_l[i]

        self.frame_count += 1

    def left_stand(self):
        self.texture = self.walk_l[0]

    def right_stand(self):
        self.texture = self.walk_r[0]

    def left_jump(self):
        self.texture = self.jump_l

    def right_jump(self):
        self.texture = self.jump_r

    def dead(self):
        if(self.right_released):
            self.texture = self.dead_r
        else:
            self.texture = self.dead_l
