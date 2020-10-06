import random, time, pygame, sys
from pygame.locals import *

# Se declaran las constantes y variables
negro = (0, 0, 0)
rojo = (255, 0, 0)
rosa = (255, 213, 213)
verde = (0, 255, 0)
azul = (0, 0, 255)
blanco = (255, 255, 255)
posicion_x = 0
posicion_y = 0
turno = 1
valido = 0
todas_las_x = {}
todas_las_o = {}
punto_coma = []
jugador = 0
todos_los_sonidos = ['beeparca.wav', 'beepspri.wav', 'applause3.wav', 'beeplaug.wav']
todas_las_posiciones = {'a1': '100;150', 'a2': '200;150', 'a3': '300;150', 'b1': '100;250', 'b2': '200;250',
                        'b3': '300;250', 'c1': '100;350', 'c2': '200;350', 'c3': '300;350'}
todas_las_posiciones_que_quedan = todas_las_posiciones


def salida(jugador):
    if jugador == 0:
        pygame.quit()
        sys.exit(0)
    if jugador == 1:
        pygame.mixer.music.load(todos_los_sonidos[3])
        pygame.mixer.music.play()
    if jugador == 2:
        pygame.mixer.music.load(todos_los_sonidos[2])
        pygame.mixer.music.play()
    time.sleep(4)
    pygame.quit()
    sys.exit(0)


# Se inicia la función principal del juego
def main():
    # Se inicializa el juego
    pygame.init()
    pygame.mixer.init()
    sysfont = pygame.font.get_default_font()
    pygame.display.set_caption("Mi Primer Jueguito de Michi")
    pantalla = pygame.display.set_mode((500, 500))
    turno = 1

    # Se inicia el bucle principal
    while True:

        # Se dibuja la pantalla y el michi vacio
        pantalla.fill(rosa)
        pygame.draw.line(pantalla, negro, (100, 250), (400, 250), 10)
        pygame.draw.line(pantalla, negro, (100, 350), (400, 350), 10)
        pygame.draw.line(pantalla, negro, (200, 150), (200, 450), 10)
        pygame.draw.line(pantalla, negro, (300, 150), (300, 450), 10)

        time.sleep(1)

        # Se dubujan todas las "x"
        px = ''
        for p, u in todas_las_x.items():
            punto_coma = u.split(';')
            posicion_x = int(punto_coma[0])
            posicion_y = int(punto_coma[1])
            pygame.draw.line(pantalla, negro, (posicion_x + 25, posicion_y + 15), (posicion_x + 75, posicion_y + 85),
                             15)
            pygame.draw.line(pantalla, negro, (posicion_x + 25, posicion_y + 85), (posicion_x + 75, posicion_y + 15),
                             15)
            px = px + p

        # Se dubujan todas las "o"
        po = ''
        for p, u in todas_las_o.items():
            punto_coma = u.split(';')
            posicion_x = int(punto_coma[0])
            posicion_y = int(punto_coma[1])
            pygame.draw.circle(pantalla, negro, (posicion_x + 50, posicion_y + 50), 38, 12)
            po = po + p
        pygame.draw.line(pantalla, rojo, (100, 200), (400, 200), 15)
        if px.find('a1') != -1 and px.find('a2') != -1 and px.find('a3') != -1:
            pygame.draw.line(pantalla, rojo, (100, 200), (400, 200), 15)
            pantalla.blit(pygame.font.SysFont(sysfont, 25).render('Ganó la Máquina', True, azul), (20, 470))
            salida(1)

        if px.find('b1') != -1 and px.find('b2') != -1 and px.find('b3') != -1:
            pygame.draw.line(pantalla, rojo, (100, 300), (400, 300), 15)
            pantalla.blit(pygame.font.SysFont(sysfont, 25).render('Ganó la Máquina', True, azul), (20, 470))
            salida(1)

        if px.find('c1') != -1 and px.find('c2') != -1 and px.find('c3') != -1:
            pygame.draw.line(pantalla, rojo, (100, 400), (400, 400), 15)
            pantalla.blit(pygame.font.SysFont(sysfont, 25).render('Ganó la Máquina', True, azul), (20, 470))
            salida(1)

        if px.find('a1') != -1 and px.find('b1') != -1 and px.find('c1') != -1:
            pygame.draw.line(pantalla, rojo, (150, 150), (150, 450), 15)
            pantalla.blit(pygame.font.SysFont(sysfont, 25).render('Ganó la Máquina', True, azul), (20, 470))
            salida(1)

        if px.find('a2') != -1 and px.find('b2') != -1 and px.find('c2') != -1:
            pygame.draw.line(pantalla, rojo, (250, 150), (250, 450), 15)
            pantalla.blit(pygame.font.SysFont(sysfont, 25).render('Ganó la Máquina', True, azul), (20, 470))
            salida(1)

        if px.find('a3') != -1 and px.find('b3') != -1 and px.find('c3') != -1:
            pygame.draw.line(pantalla, rojo, (350, 150), (350, 450), 15)
            pantalla.blit(pygame.font.SysFont(sysfont, 25).render('Ganó la Máquina', True, azul), (20, 470))
            salida(1)

        if px.find('a1') != -1 and px.find('b2') != -1 and px.find('c3') != -1:
            pygame.draw.line(pantalla, rojo, (100, 150), (150, 450), 15)
            pantalla.blit(pygame.font.SysFont(sysfont, 25).render('Ganó la Máquina', True, azul), (20, 470))
            salida(1)

        if px.find('a3') != -1 and px.find('b2') != -1 and px.find('c1') != -1:
            pygame.draw.line(pantalla, rojo, (100, 450), (400, 150), 15)
            pantalla.blit(pygame.font.SysFont(sysfont, 25).render('Ganó la Máquina', True, azul), (20, 470))
            salida(1)

        if po.find('a1') != -1 and po.find('a2') != -1 and po.find('a3') != -1:
            pygame.draw.line(pantalla, rojo, (100, 200), (400, 200), 15)
            pantalla.blit(pygame.font.SysFont(sysfont, 25).render('Ganaste', True, azul), (20, 470))
            salida(2)

        if po.find('b1') != -1 and po.find('b2') != -1 and po.find('b3') != -1:
            pygame.draw.line(pantalla, rojo, (100, 300), (400, 300), 15)
            pantalla.blit(pygame.font.SysFont(sysfont, 25).render('Ganaste', True, azul), (20, 470))
            salida(2)

        if po.find('c1') != -1 and po.find('c2') != -1 and po.find('c3') != -1:
            pygame.draw.line(pantalla, rojo, (100, 400), (400, 400), 15)
            pantalla.blit(pygame.font.SysFont(sysfont, 25).render('Ganaste', True, azul), (20, 470))
            salida(2)

        if po.find('a1') != -1 and po.find('b1') != -1 and po.find('c1') != -1:
            pygame.draw.line(pantalla, rojo, (150, 150), (150, 450), 15)
            pantalla.blit(pygame.font.SysFont(sysfont, 25).render('Ganaste', True, azul), (20, 470))
            salida(2)

        if po.find('a2') != -1 and po.find('b2') != -1 and po.find('c2') != -1:
            pygame.draw.line(pantalla, rojo, (250, 150), (250, 450), 15)
            pantalla.blit(pygame.font.SysFont(sysfont, 25).render('Ganaste', True, azul), (20, 470))
            salida(2)

        if po.find('a3') != -1 and po.find('b3') != -1 and po.find('c3') != -1:
            pygame.draw.line(pantalla, rojo, (350, 150), (350, 450), 15)
            pantalla.blit(pygame.font.SysFont(sysfont, 25).render('Ganaste', True, azul), (20, 470))
            salida(2)

        if po.find('a1') != -1 and po.find('b2') != -1 and po.find('c3') != -1:
            pygame.draw.line(pantalla, rojo, (100, 150), (150, 450), 15)
            pantalla.blit(pygame.font.SysFont(sysfont, 25).render('Ganaste', True, azul), (20, 470))
            salida(2)

        if po.find('a3') != -1 and po.find('b2') != -1 and po.find('c1') != -1:
            pygame.draw.line(pantalla, rojo, (100, 450), (400, 150), 15)
            pantalla.blit(pygame.font.SysFont(sysfont, 25).render('Ganaste', True, azul), (20, 470))
            salida(2)

        if todas_las_posiciones_que_quedan == {}:
            pantalla.blit(pygame.font.SysFont(sysfont, 25).render('Empataste con la Máquina', True, azul), (20, 470))
            salida(3)

        # Se determina el turno
        if turno == 1:
            posiciones_libres = []
            ubicacion = ''
            for p, u in todas_las_posiciones_que_quedan.items():
                posiciones_libres.append(p)
            posicion_aleatoria = random.choice(posiciones_libres)
            ubicacion = todas_las_posiciones_que_quedan.pop(posicion_aleatoria)
            punto_coma = ubicacion.split(';')
            posicion_x = int(punto_coma[0])
            posicion_y = int(punto_coma[1])
            pygame.draw.line(pantalla, rojo, (posicion_x + 25, posicion_y + 15), (posicion_x + 75, posicion_y + 85), 15)
            pygame.draw.line(pantalla, rojo, (posicion_x + 25, posicion_y + 85), (posicion_x + 75, posicion_y + 15), 15)
            todas_las_x.update({posicion_aleatoria: ubicacion})
            turno = 2
        elif turno == 2:
            valido = 0
            while valido == 0:
                for event in pygame.event.get():
                    # Sale del juego al presionar la "x" de la ventana
                    if event.type == QUIT:
                        salida(0)
                    # Al presionar los botones del mouse
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        # Al presionar el boton izquierdo
                        if event.button == 1:
                            posicion = ''
                            for p, u in todas_las_posiciones_que_quedan.items():
                                punto_coma = u.split(';')
                                posicion_x = int(punto_coma[0])
                                posicion_y = int(punto_coma[1])
                                if mouse_pos[0] in list(range(posicion_x, posicion_x + 100)) and mouse_pos[1] in list(
                                        range(posicion_y, posicion_y + 100)):
                                    pygame.draw.circle(pantalla, rojo, (posicion_x + 50, posicion_y + 50), 38, 12)
                                    todas_las_o.update({p: u})
                                    posicion = p
                                    turno = 1
                                    valido = 1
                            if valido == 1:
                                todas_las_posiciones_que_quedan.pop(posicion)
                                pygame.mixer.music.load(todos_los_sonidos[0])
                                pygame.mixer.music.play()
                            else:
                                pygame.mixer.music.load(todos_los_sonidos[1])
                                pygame.mixer.music.play()
                        # Sale del juego al presionar el boton derecho dl mouse
                        if event.button == 3:
                            salida(0)
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            salida(0)
                        else:
                            pygame.mixer.music.load(todos_los_sonidos[1])
                            pygame.mixer.music.play()
        # Se actualiza la pantalla
        # pygame.display.update()
        pygame.display.flip()


# Este fichero es el que ejecuta el juego principal
if __name__ == '__main__':
    main()
















