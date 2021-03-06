import pygame.font

class Scoreboard():

    def __init__(self,ai_settings,screen,stats):

        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # Prepare the initial score image.
        
    def show_score(self,puntaje):
        score_str  = str(puntaje)
        self.score_image = self.font.render(score_str, True, (255,255,255),(81,54,135,255))
        #display 
        self.score_rect = self.score_image.get_rect()
        #self.score_rect_right = self.screen_rect.right - 20
        self.score_rect.top = 20
        self.screen.blit(self.score_image,(1240/2, 10))