class Settings():
    """ Clase para almacenar todos los ajustes del juego"""

    def __init__(self):
        """ inica los ajustes del juego"""

        # ajustes de pantalla

        self.screen_width = 1280
        self.screen_height = 720

        #enemigos speed factor

        self.alien_speed_factor = 3

        # limite de vidas

        self.ship_limit = 4

        self.puntaje = 0

        #banderas de dificultad
        self.activo = True
    
