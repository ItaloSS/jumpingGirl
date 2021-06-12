import pygame
class Perro():
    """ inicia el personaje y su posicion inicial"""

    def __init__(self, screen):
        
        self.screen = screen

        self.image1 = pygame.image.load("jumping_girl/Images/bigotes1.png")
        self.image2 = pygame.image.load("jumping_girl/Images/bigotes2.png")
        self.image3 = pygame.image.load("jumping_girl/Images/bigotes3.png")
        self.image4 = pygame.image.load("jumping_girl/Images/bigotes4.png")
        self.image5 = pygame.image.load("jumping_girl/Images/bigotes5.png")
        self.image6 = pygame.image.load("jumping_girl/Images/bigotes6.png")
        self.image7 = pygame.image.load("jumping_girl/Images/bigotes7.png")
        self.image8 = pygame.image.load("jumping_girl/Images/bigotes8.png")


        self.rect = self.image1.get_rect()
        #self.rect2 = self.image2.get_rect()
        #self.rect3 = self.image3.get_rect()
        #self.rect4 = self.image4.get_rect()
        #self.rect5 = self.image5.get_rect()
        self.screen_rect = screen.get_rect()

        self.images = [self.image1,self.image2,self.image3,self.image4,self.image5,self.image6,self.image7,self.image8]
        #self.rects = [self.rect,self.rect2,self.rect3,self.rect4,self.rect5]        
        self.rect.x = 10
        self.rect.y = 590
        # bandera de movimiento 
        self.moving_right = False
        self.moving_left = False
        #contador
        self.contador = 0
    def update(self):
        if self.moving_right:
            self.rect.x += 12
        if self.moving_left:
            self.rect.x -= 12

    def blitme(self):
        if self.contador <= 5:
            #blitme(0)
            self.screen.blit(self.images[0], self.rect)
            self.contador +=1
        elif self.contador >= 5 and self.contador < 10:
            #blitme(1)
            self.screen.blit(self.images[1], self.rect)
            self.contador +=1
        elif self.contador >= 10 and self.contador < 15:
            #blitme(2)
            self.screen.blit(self.images[2], self.rect)
            self.contador +=1
        elif self.contador >= 15 and self.contador < 20:
            #blitme(3)
            self.screen.blit(self.images[3], self.rect)
            self.contador +=1
        elif self.contador >= 20 and self.contador <= 25:
            #blitme(4)
            self.screen.blit(self.images[4], self.rect)
            self.contador +=1
        elif self.contador >= 25 and self.contador <= 30:
            #blitme(4)
            self.screen.blit(self.images[5], self.rect)
            self.contador +=1
        elif self.contador >= 30 and self.contador <= 35:
            #blitme(4)
            self.screen.blit(self.images[6], self.rect)
            self.contador +=1
        elif self.contador >= 35 and self.contador <= 40:
            #blitme(4)
            self.screen.blit(self.images[7], self.rect)
            self.contador +=1

        else:
            self.contador = 0

