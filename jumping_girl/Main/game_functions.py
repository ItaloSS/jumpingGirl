import sys

import pygame
from alien import Alien
import random
#pylint: disable=no-member
def check_events(ship,stats, play_button,enemigos,bigotes):
    """ responde a los eventos de teclado y mouse """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship,bigotes)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship,bigotes)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_button_juega(stats, play_button,mouse_x,mouse_y)
    
def check_button_juega(stats, play_button,mouse_x,mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        
def check_keydown_events(event,ship,bigotes):
    """responde al presionar un boton"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        bigotes.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        bigotes.moving_left = True
    elif event.key == pygame.K_SPACE:
        ship.jumping = True
def check_keyup_events(event,ship,bigotes):
    """ responde al soltar un boton"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
        bigotes.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
        bigotes.moving_left = False
        

def create_fleet(ai_settings,screen):
    lista = []
    for i in range(6):
        alien = Alien(ai_settings,screen,random.randint(0,2))
        alien.rect.x = 900 + 600*i
        lista.append(alien)


    return lista

def update_aliens(alien):
    alien.update()

def update_collitions(ai_settings,stats,screen,ship,alien,enemigos):
    if ship.rect.colliderect(alien.rect):
        ship_hit(ai_settings,stats,screen,ship)
        posicion = alien_mas_lejos(enemigos)
        alien.rect.x = posicion + 600
    

def update_enemigo(ai_settings,screen,enemigos,sb):
    for alien in enemigos:
        if alien.rect.x < - alien.rect.width:
            ai_settings.puntaje += 10
            #alien.rect.x = enemigos[-1].rect.x + 500
            posicion = alien_mas_lejos(enemigos)
            alien.rect.x = posicion + 600
        elif alien.rect.x < - alien.rect.width and ai_settings.puntaje > 100 :
            ai_settings.puntaje += 10
            #alien.rect.x = enemigos[-1].rect.x + 500
            posicion = alien_mas_lejos(enemigos)
            alien.rect.x = posicion + random.randint(500,600)
        elif alien.rect.x < - alien.rect.width and ai_settings.puntaje > 200 :
            ai_settings.puntaje += 10
            #alien.rect.x = enemigos[-1].rect.x + 500
            posicion = alien_mas_lejos(enemigos)
            alien.rect.x = posicion + random.randint(400,600)
        elif alien.rect.x < - alien.rect.width and ai_settings.puntaje > 300 :
            ai_settings.puntaje += 10
            #alien.rect.x = enemigos[-1].rect.x + 500
            posicion = alien_mas_lejos(enemigos)
            alien.rect.x = posicion + random.randint(300,600)
        elif alien.rect.x < - alien.rect.width and ai_settings.puntaje > 400 :
            ai_settings.puntaje += 10
            #alien.rect.x = enemigos[-1].rect.x + 500
            posicion = alien_mas_lejos(enemigos)
            alien.rect.x = posicion + random.randint(300,500)
        elif alien.rect.x < - alien.rect.width and ai_settings.puntaje > 500 :
            ai_settings.puntaje += 10
            #alien.rect.x = enemigos[-1].rect.x + 500
            posicion = alien_mas_lejos(enemigos)
            alien.rect.x = posicion + random.randint(300,350)

    sb.show_score(ai_settings.puntaje)
def ship_hit(ai_settings,stats,screen,ship):
    #quita vidas
    if stats.ships_left > 0:
        stats.ships_left -= 1

        
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def alien_mas_lejos(enemigos):
    lista_de_posiciones = []
    for alien in enemigos:
        lista_de_posiciones.append(alien.rect.x)
    return max(lista_de_posiciones)

def resetear_posiciones(ship,enemigos,bigotes):

    ship.rect.x = 100
    bigotes.rect.x = 10
    for i in range(0,len(enemigos)):
        enemigos[i].rect.x = 900 + 600*i

def lives_left(stats,luna,screen):
    for vida in range(stats.ships_left):
        screen.blit(luna,(950 + vida*70,0))

def aumentar_dficultad(ai_settings):
    if ai_settings.puntaje != 0:
        if ai_settings.puntaje % 50 == 0 and ai_settings.activo:
            ai_settings.alien_speed_factor += 1
            ai_settings.activo = False
        elif  ai_settings.puntaje % 60 == 0 and not ai_settings.puntaje % 50 == 0 :
            ai_settings.activo = True
            


            
            


    

        