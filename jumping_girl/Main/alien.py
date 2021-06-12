import pygame

class Alien():
    
    def __init__(self,ai_settings,screen,indice):
        self.screen = screen
        self.ai_settings = ai_settings

        if indice == 0 : 
            self.image = pygame.image.load("jumping_girl/Images/enemigo.png")
            self.rect = self.image.get_rect()
            self.rect.x = 900 
            self.rect.y = 510
        else :
            self.image = pygame.image.load("jumping_girl/Images/enemigo1.png")
            self.rect = self.image.get_rect()
            self.rect.x = 900 
            self.rect.y = 500


    def blitme(self):
        self.screen.blit(self.image, self.rect)
        

    def update(self):
        """  mueve los enemigos """
        self.rect.x -= self.ai_settings.alien_speed_factor
        
        
