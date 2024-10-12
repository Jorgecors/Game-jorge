import pygame
import sys
import subprocess
from pygame.locals import *

pygame.init()

color = (255, 255, 0)
altura = 426
ancho = 640
pantalla = pygame.display.set_mode((ancho, altura))
pygame.display.set_caption("Juego :D")

# Cargar la imagen y escalarla para que coincida con las dimensiones de la pantalla
fondo = pygame.image.load("imagenes/waka.jpeg")
fondo = pygame.transform.scale(fondo, (ancho, altura))

menu_botones = ["New Game", "Quit"]

boton_altura = 200
boton_ancho = 50

button_rects = []
button_rects.append(pygame.Rect(ancho / 4, altura / 3, boton_altura, boton_ancho))
button_rects.append(pygame.Rect(ancho / 4, altura / 3 + 70, boton_altura, boton_ancho))
button_rects.append(pygame.Rect(ancho / 4, altura / 3 + 140, boton_altura, boton_ancho))
button_rects.append(pygame.Rect(ancho / 4, altura / 3 + 210, boton_altura, boton_ancho))

selected_index = 0

mouse_clicked = False

font = pygame.font.Font(None, 36)

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked = True
            mouse_pos = pygame.mouse.get_pos()
            for i, rect in enumerate(button_rects):
                if rect.collidepoint(mouse_pos):
                    if i == 0:
                        # Abrir la interfaz del juego usando subprocess
                        subprocess.Popen(['python', 'game.py'])
                    elif i == 1:
                        print("Load game selected")
                    elif i == 2:    
                        print("Settings selected")
                    elif i == 3:
                        running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_clicked = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_index = (selected_index - 1) % len(menu_botones)
            elif event.key == pygame.K_DOWN:
                selected_index = (selected_index + 1) % len(menu_botones)
            elif event.key == pygame.K_RETURN:
                if menu_botones[selected_index] == "New Game":
                    # Abrir la interfaz del juego usando subprocess
                    subprocess.Popen(['python', 'game.py'])
               
                elif menu_botones[selected_index] == "Settings":
                    print("Settings selected")
                elif menu_botones[selected_index] == "Quit":
                    running = False

    pantalla.blit(fondo, (0, 0))  # Dibujar la imagen de fondo
    
    for i, item in enumerate(menu_botones):
        text = font.render(item, True, color)
        text_rect = text.get_rect(center=button_rects[i].center)
        if i == selected_index:
            pygame.draw.rect(pantalla, (100, 100, 100), button_rects[i], 2)        
    
        pygame.draw.rect(pantalla, (255,255, 255), button_rects[i])
  
        pantalla.blit(text, text_rect)

    # Refresh the screen
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
