import pygame


class EnemyAnimation(object):

    def __init__(self, walk_l, walk_r, dead_l, dead_r):
        # Deze class krijgt een object enemy mee. Het is mogelijk de afbeeldingen in de
        # constructor toe te voegen, maar dit lijkt me overbodig omdat je de lijsten
        # uit de enemy kan halen
        self.walk_l = walk_l
        self.walk_r = walk_r
        self.dead_l = dead_l
        self.dead_r = dead_r

        # texture is de afbeelding. Er moet een default afbeelding mee gegeven worden anders is
        # de var in het eerste frame leeg. Hierdoor krijg je een error
        self.texture = self.walk_l[0]

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


    def update(self, xSpeed, dead):
        if xSpeed > 0:
            self.right_walk()
            self.left_released = False
            self.right_released = True
        elif xSpeed < 0:
            self.left_walk()
            self.left_released = True
            self.right_released = False

        if dead:
            self.dead()

        return self.texture

    def right_walk(self):
        if self.frame_count >= self.frame_cap:
            self.frame_count = 0

        for i in range(self.length_list):
            if self.frame_count / self.tex_switch == i:
                self.texture = self.walk_r[i]

        self.frame_count += 1

    def left_walk(self):
        if self.frame_count >= self.frame_cap:
            self.frame_count = 0

        for i in range(self.length_list):
            if self.frame_count / self.tex_switch == i:
                self.texture = self.walk_l[i]

        self.frame_count += 1

    def dead(self):
        if self.right_released:
            self.texture = self.dead_r
        else:
            self.texture = self.dead_l
