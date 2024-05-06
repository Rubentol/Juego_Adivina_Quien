import pygame
import random
import sys

pygame.init()

COLOR = (200,200,200)

ANCHO = 1100
ALTO = 600

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego Adivina Quien")

# Cargar la imagen de fondo
fondo = pygame.image.load("Fondo.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

# Crear un objeto de fuente
titulo = pygame.font.Font(None, 50)
bienvenidos = pygame.font.Font(None, 32)
instru = pygame.font.Font(None, 32)
play = pygame.font.Font(None, 32)
Exce = pygame.font.Font(None, 32)
Como = pygame.font.Font(None, 32)
Rein = pygame.font.Font(None, 32)

Peg1 = pygame.font.Font(None, 32)
Peg2 = pygame.font.Font(None, 32)
Peg3 = pygame.font.Font(None, 32)
Peg4 = pygame.font.Font(None, 32)
Peg5 = pygame.font.Font(None, 32)
Peg6 = pygame.font.Font(None, 32)
Peg7 = pygame.font.Font(None, 32)
Peg8 = pygame.font.Font(None, 32)
Muj1 = pygame.font.Font(None, 32)
Anita = pygame.font.Font(None, 32)

# Renderizar el texto
titulo = titulo.render("Juego Adivina Quien de Ruben Dios <3", True, COLOR)
bienvenidos = bienvenidos.render("Bienvenido al Juego Adivina Quien!", True, COLOR)
instru = instru.render("Elije un Personaje para Convensar", True, COLOR)
Exce = Exce.render("Excelente!", True, COLOR)
Como = Como.render("Como Que No!", True, COLOR)
Rein = Rein.render("Preciona Reiniciar", True, COLOR)

play = play.render("Preciona play!", True, COLOR)
Peg1 = Peg1.render("Tu Personaje es Hombre?", True, COLOR)
Peg2 = Peg2.render("Sus ojos son Cafes?", True, COLOR)
Peg3 = Peg3.render("Tiene el Cabello Negro?", True, COLOR)
Peg4 = Peg4.render("Usa Sombrero?", True, COLOR)
Peg5 = Peg5.render("Tu Personaje es Rubio?", True, COLOR)
Peg6 = Peg6.render("Tu Personaje es Rubio?", True, COLOR)
Peg7 = Peg7.render("Tiene el Cabello Blanco?", True, COLOR)
Peg8 = Peg8.render("Tu Personaje esta Medio Pelon?", True, COLOR)


Muj1 = Muj1.render("Tu Personaje es Rubia?", True, COLOR)
Anita = Anita.render("Tu Personaje es:", True, COLOR)

# Obtener el rectángulo del texto para centrarlo en la ventana
titulo_rect = titulo.get_rect(center=(ANCHO//2, ALTO//11))
bienvenidos_rect = bienvenidos.get_rect(center=(ANCHO//5, ALTO//4.5))
instru_rect = instru.get_rect(center=(ANCHO//5, ALTO//3.25))

play_rect = play.get_rect(center=(ANCHO//5, ALTO//2.5))
Rein_rect = Rein.get_rect(center=(ANCHO//5, ALTO//2.5))
Peg1_rect = Peg1.get_rect(center=(ANCHO//5, ALTO//3.5))
Peg2_rect = Peg2.get_rect(center=(ANCHO//5, ALTO//3.5))
Peg3_rect = Peg3.get_rect(center=(ANCHO//5, ALTO//3.5))
Peg4_rect = Peg4.get_rect(center=(ANCHO//5, ALTO//3.5))
Peg5_rect = Peg5.get_rect(center=(ANCHO//5, ALTO//3.5))
Peg6_rect = Peg6.get_rect(center=(ANCHO//5, ALTO//3.5))
Peg7_rect = Peg7.get_rect(center=(ANCHO//5, ALTO//3.5))
Peg8_rect = Peg8.get_rect(center=(ANCHO//5, ALTO//3.5))

Muj1_rect = Muj1.get_rect(center=(ANCHO//5, ALTO//3.5))
Anita_rect = Anita.get_rect(center=(ANCHO//5, ALTO//3.5))

Como_rect = Como.get_rect(center=(ANCHO//5, ALTO//3.5))
Exce_rect = Exce.get_rect(center=(ANCHO//5, ALTO//3.5))

# Cargar la imagen de los personajes
personajes = pygame.image.load("Personajes.jpg")
    #Para Respuestas 
Per_Alex = pygame.image.load("Alex.jpg")
Per_Alex = pygame.transform.scale(Per_Alex, (ANCHO // 9, ALTO // 5))
Per_Alfred = pygame.image.load("Alfred.jpg")
Per_Alfred = pygame.transform.scale(Per_Alfred, (ANCHO // 9, ALTO // 5))
Per_Anita = pygame.image.load("Anita.jpg")
Per_Anita = pygame.transform.scale(Per_Anita, (ANCHO // 9, ALTO // 5))
Per_Anne = pygame.image.load("Anne.jpg")
Per_Anne = pygame.transform.scale(Per_Anne, (ANCHO // 9, ALTO // 5))
Per_Bernard = pygame.image.load("Bernard.jpg")
Per_Bernard = pygame.transform.scale(Per_Bernard, (ANCHO // 9, ALTO // 5))
Per_David = pygame.image.load("David.jpg")
Per_David = pygame.transform.scale(Per_David, (ANCHO // 9, ALTO // 5))
Per_Eric = pygame.image.load("Eric.jpg")
Per_Eric = pygame.transform.scale(Per_Eric, (ANCHO // 9, ALTO // 5))
Per_Frans = pygame.image.load("Frans.jpg")
Per_Frans = pygame.transform.scale(Per_Frans, (ANCHO // 9, ALTO // 5))
Per_George = pygame.image.load("George.jpg")
Per_George = pygame.transform.scale(Per_George, (ANCHO // 9, ALTO // 5))
Per_Herman = pygame.image.load("Herman.jpg")
Per_Herman = pygame.transform.scale(Per_Herman, (ANCHO // 9, ALTO // 5))
Bob = pygame.image.load("Bob.jpg")
Bob = pygame.transform.scale(Bob, (ANCHO // 9, ALTO // 5))
Excelente = pygame.image.load("EXCELENTE.jpg")
Excelente = pygame.transform.scale(Excelente, (ANCHO // 9, ALTO // 5))
ComoNo = pygame.image.load("COMOQUENO.jpg")
ComoNo = pygame.transform.scale(ComoNo, (ANCHO // 9, ALTO // 5))
    #Botonoes 
boton_no_img = pygame.image.load("NO.jpg") #NO
boton_no_img = pygame.transform.scale(boton_no_img, (ANCHO // 8, ALTO // 12))
boton_si_img = pygame.image.load("YES.jpg") #YES
boton_si_img = pygame.transform.scale(boton_si_img, (ANCHO // 8, ALTO // 12))
boton_play_img = pygame.image.load("PLAY.jpg") #PLAY
boton_play_img = pygame.transform.scale(boton_play_img, (ANCHO // 8, ALTO // 12))
boton_salir_img = pygame.image.load("SALIR.png") #SALIR
boton_salir_img = pygame.transform.scale(boton_salir_img, (ANCHO // 8, ALTO // 12))
boton_reiniciar_img = pygame.image.load("reiniciar.png") #SALIR
boton_reiniciar_img = pygame.transform.scale(boton_reiniciar_img, (ANCHO // 10, ALTO // 10))

# Definir la posición de los botones
boton_no_rect = boton_no_img.get_rect()
boton_no_rect.center = (ANCHO // 8, ALTO // 1.35)
boton_si_rect = boton_si_img.get_rect()
boton_si_rect.center = (ANCHO // 3.7, ALTO // 1.35)
boton_play_rect = boton_play_img.get_rect()
boton_play_rect.center = (ANCHO // 5, ALTO // 1.15)
boton_salir_rect = boton_salir_img.get_rect()
boton_salir_rect.center = (ANCHO // 1.1, ALTO // 1.05)
boton_reiniciar_rect = boton_reiniciar_img.get_rect()
boton_reiniciar_rect.center = (ANCHO // 8, ALTO // 8)

Personajes = [
    {"nombre": "Alex", "sexo": "masculino", "color_pelo": "negro", "gorro": "no", "color_ojos": "cafes claro"},
    {"nombre": "Alfred", "sexo": "masculino", "color_pelo": "pelirrojo", "gorro": "no", "color_ojos": "azules"},
    {"nombre": "Anita", "sexo": "femenino", "color_pelo": "Rubio", "gorro": "no", "color_ojos": "azules"},
    {"nombre": "Anne", "sexo": "femenino", "color_pelo": "negro", "gorro": "no", "color_ojos": "cafes"},
    {"nombre": "Bernard", "sexo": "masculino", "color_pelo": "castaño", "gorro": "si", "color_ojos": "cafes"},
    {"nombre": "David", "sexo": "masculino", "color_pelo": "Rubio", "gorro": "no", "color_ojos": "cafes claro"},
    {"nombre": "Eric", "sexo": "masculino", "color_pelo": "Rubio", "gorro": "si", "color_ojos": "cafes"},
    {"nombre": "Frans", "sexo": "masculino", "color_pelo": "pelirrojo", "gorro": "no", "color_ojos": "cafes"},
    {"nombre": "George", "sexo": "masculino", "color_pelo": "blanco", "gorro": "si", "color_ojos": "cafes"},
    {"nombre": "Herman", "sexo": "masculino", "color_pelo": "pelirrojo", "gorro": "no", "color_ojos": "cafe claro"},
    
]   

# Define el tipo de evento personalizado
MI_EVENTO = pygame.USEREVENT + 1

# Define el tiempo de espera en milisegundos (por ejemplo, 3000ms = 3 segundos)
tiempo_espera = 1000



def abrir_ventana():
    mostrar_play = True
    mostrar_Exce = False
    mostrar_Como =False

    mostrar_Peg1 = False
    mostrar_Peg2 = False
    mostrar_Peg3 = False
    mostrar_Peg4 = False
    mostrar_Peg5 = False
    mostrar_Peg6 = False
    mostrar_Peg7 = False
    mostrar_Peg8 = False

    mostrar_Muj1 = False

    mostrar_Anita = False
    mostrar_Anne = False
    mostrar_Alfred = False
    mostrar_Alex = False
    mostrar_Erick = False
    mostrar_David =False
    mostrar_George = False
    mostrar_Bernard = False
    mostrar_Herman = False
    mostrar_Frans = False

    REINICIAR = False
    opc1 = False
    opc2 = False 
    opc3 = False
    opc4 = False
    opc5 = False
    opc6 = False
    opc7 = False
    opc8 = False
    opc9 = False 
    opc10 =False
    opc11 = False 
    opc12 =False
    opc13 = False
    opc14 = False
    opc15 = False
    opc16 = False
    opc17 = False
    opc18 = False

    pygame.time.set_timer(MI_EVENTO, tiempo_espera)

    while True: 

        #Dibujar Ventana
        ventana.fill(COLOR)
        ventana.blit(fondo, (0, 0))
        #Personajes Imagen Grande
        ventana.blit(personajes, (1500 // 2 - personajes.get_width() // 2, 110))
         
        #Titulo, Bienvenida, Intruciones 
        ventana.blit(titulo, titulo_rect) 
        ventana.blit(bienvenidos, bienvenidos_rect)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_salir_rect.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()
                elif boton_reiniciar_rect.collidepoint(evento.pos):
                    mostrar_play = True
                    mostrar_Exce = False
                    mostrar_Como =False

                    mostrar_Peg1 = False
                    mostrar_Peg2 = False
                    mostrar_Peg3 = False
                    mostrar_Peg4 = False
                    mostrar_Peg5 = False
                    mostrar_Peg6 = False
                    mostrar_Peg7 = False
                    mostrar_Peg8 = False

                    mostrar_Muj1 = False

                    mostrar_Anita = False
                    mostrar_Anne = False
                    mostrar_Alfred = False
                    mostrar_Alex = False
                    mostrar_Erick = False
                    mostrar_David = False
                    mostrar_George = False
                    mostrar_Bernard = False
                    mostrar_Herman = False
                    mostrar_Frans = False

                    REINICIAR = False
                    opc1 = False
                    opc2 = False 
                    opc3 = False
                    opc4 = False
                    opc5 = False
                    opc6 = False
                    opc7 = False
                    opc8 = False
                    opc9 = False 
                    opc10 =False
                    opc11 = False 
                    opc12 =False 
                    opc13 = False
                    opc14 = False
                    opc15 = False
                    opc16 = False
                    opc17 = False
                    opc18 = False
                elif (boton_play_rect.collidepoint(evento.pos) and not REINICIAR) or mostrar_Peg1:
                    REINICIAR = True
                    mostrar_play = False
                    mostrar_Peg1 = True
                    if boton_si_rect.collidepoint(evento.pos):
                        mostrar_Peg2 = True
                        mostrar_Peg1 = False
                    elif boton_no_rect.collidepoint(evento.pos):
                        mostrar_Muj1 = True
                        mostrar_Peg1 = False

                

        if mostrar_play:
            ventana.blit(play, play_rect)
            ventana.blit(instru, instru_rect)
            mostrar_Peg1 = False
            mostrar_Peg2 = False
            mostrar_Peg3 = False
            mostrar_Muj1 = False
            
        if mostrar_Peg1:
            ventana.blit(Peg1, Peg1_rect)
            ventana.blit(Bob, (975 // 2 - personajes.get_width() // 2, 195))
                
        if mostrar_Peg2:
            if evento.type == MI_EVENTO or opc1:
                opc1 = True
                ventana.blit(Peg2, Peg2_rect)
                ventana.blit(Bob, (975 // 2 - personajes.get_width() // 2, 195))
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_si_rect.collidepoint(evento.pos):
                        mostrar_Peg3 = True
                        mostrar_Peg2 = False
                    elif boton_no_rect.collidepoint(evento.pos):
                        mostrar_Alfred = True
                        mostrar_Peg2 = False
        
        if mostrar_Peg3:
            if evento.type == MI_EVENTO or opc6:
                opc6 = True
                ventana.blit(Peg3, Peg3_rect)
                ventana.blit(Bob, (975 // 2 - personajes.get_width() // 2, 195))
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_si_rect.collidepoint(evento.pos):
                        mostrar_Alex = True
                        mostrar_Peg3 = False
                    elif boton_no_rect.collidepoint(evento.pos):
                        mostrar_Peg4 = True
                        mostrar_Peg3 = False
        
        if mostrar_Peg4:
            if evento.type == MI_EVENTO or opc8:
                opc8 = True
                ventana.blit(Peg4, Peg4_rect)
                ventana.blit(Bob, (975 // 2 - personajes.get_width() // 2, 195))
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_si_rect.collidepoint(evento.pos):
                        mostrar_Peg5 = True
                        mostrar_Peg4 = False
                    elif boton_no_rect.collidepoint(evento.pos):
                        mostrar_Peg6 = True
                        mostrar_Peg4 = False
        
        if mostrar_Peg5:
            if evento.type == MI_EVENTO or opc9:
                opc9 = True
                ventana.blit(Peg5, Peg5_rect)
                ventana.blit(Bob, (975 // 2 - personajes.get_width() // 2, 195))
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_si_rect.collidepoint(evento.pos):
                        mostrar_Erick = True
                        mostrar_Peg5 = False
                    elif boton_no_rect.collidepoint(evento.pos):
                        mostrar_Peg7 = True
                        mostrar_Peg5 = False

        if mostrar_Peg6:
            if evento.type == MI_EVENTO or opc11:
                opc11 = True
                ventana.blit(Peg6, Peg6_rect)
                ventana.blit(Bob, (975 // 2 - personajes.get_width() // 2, 195))
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_si_rect.collidepoint(evento.pos):
                        mostrar_David = True
                        mostrar_Peg6 = False
                    elif boton_no_rect.collidepoint(evento.pos):
                        mostrar_Peg8 = True
                        mostrar_Peg6 = False

        if mostrar_Peg7:
            if evento.type == MI_EVENTO or opc13:
                opc13 = True
                ventana.blit(Peg7, Peg7_rect)
                ventana.blit(Bob, (975 // 2 - personajes.get_width() // 2, 195))
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_si_rect.collidepoint(evento.pos):
                        mostrar_George = True
                        mostrar_Peg7 = False
                    elif boton_no_rect.collidepoint(evento.pos):
                        mostrar_Bernard = True
                        mostrar_Peg7 = False

        if mostrar_Peg8:
            if evento.type == MI_EVENTO or opc14:
                opc14 = True
                ventana.blit(Peg8, Peg8_rect)
                ventana.blit(Bob, (975 // 2 - personajes.get_width() // 2, 195))
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_si_rect.collidepoint(evento.pos):
                        mostrar_Herman = True
                        mostrar_Peg8 = False
                    elif boton_no_rect.collidepoint(evento.pos):
                        mostrar_Frans = True
                        mostrar_Peg8 = False

        if mostrar_Muj1:
            if evento.type == MI_EVENTO or opc2:
                opc2 = True
                ventana.blit(Muj1, Muj1_rect)
                ventana.blit(Bob, (975 // 2 - personajes.get_width() // 2, 195))
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_si_rect.collidepoint(evento.pos):
                        mostrar_Anita = True
                        mostrar_Muj1 = False
                    elif boton_no_rect.collidepoint(evento.pos):
                        mostrar_Anne = True
                        mostrar_Muj1 = False

        if mostrar_Anita:
            mostrar_Muj1 = False
            if evento.type == MI_EVENTO or opc3:
                opc3 = True
                ventana.blit(Anita, Anita_rect)
                ventana.blit(Per_Anita, (975 // 2 - personajes.get_width() // 2, 260))
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_si_rect.collidepoint(evento.pos):
                        mostrar_Exce = True
                    elif boton_no_rect.collidepoint(evento.pos):
                        mostrar_Como = True

        if mostrar_Anne:
            mostrar_Muj1 = False
            if evento.type == MI_EVENTO or opc4:
                opc4 = True 
                ventana.blit(Anita, Anita_rect)
                ventana.blit(Per_Anne, (975 // 2 - personajes.get_width() // 2, 260))
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_si_rect.collidepoint(evento.pos):
                        mostrar_Exce = True
                    elif boton_no_rect.collidepoint(evento.pos):
                        mostrar_Como = True
          
        if mostrar_Alfred: 
            mostrar_Peg2 = False
            if evento.type == MI_EVENTO or opc5:
                opc5 = True
                ventana.blit(Anita, Anita_rect)
                ventana.blit(Per_Alfred, (975 // 2 - personajes.get_width() // 2, 260))
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_si_rect.collidepoint(evento.pos):
                        mostrar_Exce = True
                    elif boton_no_rect.collidepoint(evento.pos):
                        mostrar_Como = True

        if mostrar_Alex: 
            mostrar_Peg3 = False
            if evento.type == MI_EVENTO or opc7:
                opc7 = True
                ventana.blit(Anita, Anita_rect)
                ventana.blit(Per_Alex, (975 // 2 - personajes.get_width() // 2, 260))
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_si_rect.collidepoint(evento.pos):
                        mostrar_Exce = True
                    elif boton_no_rect.collidepoint(evento.pos):
                        mostrar_Como = True

        if mostrar_Erick: 
            mostrar_Peg5 = False
            if evento.type == MI_EVENTO or opc10:
                opc10 = True
                ventana.blit(Anita, Anita_rect)
                ventana.blit(Per_Eric, (975 // 2 - personajes.get_width() // 2, 260))
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_si_rect.collidepoint(evento.pos):
                        mostrar_Exce = True
                    elif boton_no_rect.collidepoint(evento.pos):
                        mostrar_Como = True
        
        if mostrar_David: 
            mostrar_Peg6 = False
            if evento.type == MI_EVENTO or opc12:
                opc12 = True
                ventana.blit(Anita, Anita_rect)
                ventana.blit(Per_David, (975 // 2 - personajes.get_width() // 2, 260))
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_si_rect.collidepoint(evento.pos):
                        mostrar_Exce = True
                    elif boton_no_rect.collidepoint(evento.pos):
                        mostrar_Como = True

        if mostrar_George: 
            mostrar_Peg7 = False
            if evento.type == MI_EVENTO or opc15:
                opc15 = True
                ventana.blit(Anita, Anita_rect)
                ventana.blit(Per_George, (975 // 2 - personajes.get_width() // 2, 260))
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_si_rect.collidepoint(evento.pos):
                        mostrar_Exce = True
                    elif boton_no_rect.collidepoint(evento.pos):
                        mostrar_Como = True
        
        if mostrar_Bernard: 
            mostrar_Peg7 = False
            if evento.type == MI_EVENTO or opc16:
                opc16 = True
                ventana.blit(Anita, Anita_rect)
                ventana.blit(Per_Bernard, (975 // 2 - personajes.get_width() // 2, 260))
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_si_rect.collidepoint(evento.pos):
                        mostrar_Exce = True
                    elif boton_no_rect.collidepoint(evento.pos):
                        mostrar_Como = True
        
        if mostrar_Herman: 
            mostrar_Peg8 = False
            if evento.type == MI_EVENTO or opc17:
                opc17 = True
                ventana.blit(Anita, Anita_rect)
                ventana.blit(Per_Herman, (975 // 2 - personajes.get_width() // 2, 260))
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_si_rect.collidepoint(evento.pos):
                        mostrar_Exce = True
                    elif boton_no_rect.collidepoint(evento.pos):
                        mostrar_Como = True

        if mostrar_Frans: 
            mostrar_Peg8 = False
            if evento.type == MI_EVENTO or opc18:
                opc18 = True
                ventana.blit(Anita, Anita_rect)
                ventana.blit(Per_Frans, (975 // 2 - personajes.get_width() // 2, 260))
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_si_rect.collidepoint(evento.pos):
                        mostrar_Exce = True
                    elif boton_no_rect.collidepoint(evento.pos):
                        mostrar_Como = True
        
        if mostrar_Como:
            mostrar_Anita = False
            mostrar_Anne = False
            mostrar_Alfred = False
            mostrar_Alex = False
            mostrar_Erick = False
            mostrar_David = False
            mostrar_George = False
            mostrar_Bernard = False
            mostrar_Herman = False
            mostrar_Frans = False
            ventana.blit(Como, Como_rect)
            ventana.blit(Rein, Rein_rect)
            ventana.blit(ComoNo, (975 // 2 - personajes.get_width() // 2, 260))

        if mostrar_Exce:
            mostrar_Anita = False
            mostrar_Anne = False
            mostrar_Alfred = False
            mostrar_Alex = False
            mostrar_Erick = False
            mostrar_David =False
            mostrar_George = False
            mostrar_Bernard = False
            mostrar_Herman = False
            mostrar_Frans = False
            ventana.blit(Exce, Exce_rect)
            ventana.blit(Rein, Rein_rect)
            ventana.blit(Excelente, (975 // 2 - personajes.get_width() // 2, 260))

      
        #Botones
        ventana.blit(boton_no_img, boton_no_rect)
        ventana.blit(boton_si_img, boton_si_rect)
        ventana.blit(boton_play_img, boton_play_rect)
        ventana.blit(boton_salir_img, boton_salir_rect)
        ventana.blit(boton_reiniciar_img, boton_reiniciar_rect)
        pygame.display.flip()

# Llamar a la función para abrir la ventana
abrir_ventana()
