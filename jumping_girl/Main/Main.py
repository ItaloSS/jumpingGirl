import pygame
import sys
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from game_stats import GameStats
from button import Button
from bigotes import Perro
from scoreboard import Scoreboard
#pylint: disable = no-member


def run_game():
    #variables necesarias e iniciacion del juego
    pygame.init()
    fps = 60
    relojdefps = pygame.time.Clock()
    
    #crea una instancia de ajustes
    ai_settings = Settings()

    #crea la superficie de la pantalla
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("jumping girl")

    # crea una instancia de la clase button 
    play_button = Button(ai_settings,screen, "Comenzar")

    # crea al personaje
    ship = Ship(screen)
    #crea bigotes
    bigotes = Perro(screen)

    #crea la cantidad de enemigos
    enemigos = gf.create_fleet(ai_settings,screen)

    #importando el fondo
    bg_image = pygame.image.load("jumping_girl/Images/sketch_fondo.jpg").convert()
    x_ct = 0
    #importanto a la luna
    luna = pygame.image.load("jumping_girl/Images/luna2.png")
    
    #crea una instancia de stats
    stats = GameStats(ai_settings)

    #importa la musica, setea su duracion y setea el volume
    pygame.mixer.music.load("jumping_girl/music/song.mp3")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.1)
    
    #crea una isntacia de scoreboard
    sb = Scoreboard(ai_settings,screen,stats)
    while True:
        #fondo 
        relative_x = x_ct % bg_image.get_rect().width
        screen.blit(bg_image,(relative_x - bg_image.get_rect().width,0))
        if relative_x < ai_settings.screen_width:
            screen.blit(bg_image, (relative_x,0))
        x_ct -= 2
        gf.lives_left(stats,luna,screen)
        #chequea los eventos 
        gf.check_events(ship,stats, play_button,enemigos,bigotes)
        gf.update_enemigo(ai_settings,screen,enemigos,sb)
        gf.aumentar_dficultad(ai_settings)
        
        if stats.game_active:
            #recarga el personaje
            ship.update()
            bigotes.update()

            #recarga los enemigos y chequea las coliciones
            for alien in enemigos:
                alien.update()
            for alien in enemigos:
                gf.update_collitions(ai_settings,stats,screen,ship,alien,enemigos)

            #blitea a los enemigos
            for alien in enemigos:
                alien.blitme()

            #blitea al personaje
            ship.blitme()
            #blitea a bigotes
            bigotes.blitme()

            #updatea el score

            
        else:
            play_button.draw_button()
            gf.resetear_posiciones(ship,enemigos,bigotes)
            ai_settings.puntaje = 0
            ai_settings.alien_speed_factor = 3
 
        #hace el dibujo mas reciente visible en la pantalla 
        pygame.display.flip()
        relojdefps.tick(fps)
if __name__ == "__main__":
    run_game()