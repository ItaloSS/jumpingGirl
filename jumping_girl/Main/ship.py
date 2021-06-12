import pygame
class Ship():
    """ inicia el personaje y su posicion inicial"""

    def __init__(self, screen):
        
        self.screen = screen

        self.image1 = pygame.image.load("jumping_girl/Images/vale1.png")
        self.image2 = pygame.image.load("jumping_girl/Images/vale2.png")
        self.image3 = pygame.image.load("jumping_girl/Images/vale2.png")
        self.image4 = pygame.image.load("jumping_girl/Images/vale2.png")
        self.image5 = pygame.image.load("jumping_girl/Images/vale2.png")

        self.rect = self.image1.get_rect()
        #self.rect2 = self.image2.get_rect()
        #self.rect3 = self.image3.get_rect()
        #self.rect4 = self.image4.get_rect()
        #self.rect5 = self.image5.get_rect()
        self.screen_rect = screen.get_rect()

        self.images = [self.image1,self.image2,self.image3,self.image4,self.image5]
        #self.rects = [self.rect,self.rect2,self.rect3,self.rect4,self.rect5]        
        self.rect.x = 100
        self.rect.y = 400

        # bandera de movimiento 
        self.moving_right = False
        self.moving_left = False
        self.jumping = False

        # variable de salto
        self.vel_y = 12

        #contador
        self.contador = 0


    def update(self):
        if self.moving_right and (self.rect.x + 100) < self.screen_rect.right:
            self.rect.x += 12
        if self.moving_left and self.rect.x > 0 :
            self.rect.x -= 12

        #jumping 
        if self.jumping:
            self.rect.y -= self.vel_y*3
            self.vel_y -= 1
            if self.vel_y < -12:
                self.jumping = False
                self.vel_y = 12
    
    def blitme(self):
        if self.contador <= 3:
            #blitme(0)
            self.screen.blit(self.images[0], self.rect)
            self.contador +=1
        elif self.contador >= 3 and self.contador < 6:
            #blitme(1)
            self.screen.blit(self.images[1], self.rect)
            self.contador +=1
        elif self.contador >= 6 and self.contador < 9:
            #blitme(2)
            self.screen.blit(self.images[2], self.rect)
            self.contador +=1
        elif self.contador >= 9 and self.contador < 12:
            #blitme(3)
            self.screen.blit(self.images[3], self.rect)
            self.contador +=1
        elif self.contador >= 12 and self.contador <= 15:
            #blitme(4)
            self.screen.blit(self.images[4], self.rect)
            self.contador +=1
        else:
            self.contador = 0

