#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame


class Personaje(pygame.sprite.Sprite):
    def __init__(self):
        self.image = personaje = pygame.image.load(
            "Imagenes/goku.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(50, 300)
        self.muerto = 0

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_SPACE]:
            self.image = personaje = pygame.image.load(
                "Imagenes/gokukamehameha.png").convert_alpha()
        elif kamehameha.rect.x > 860:
            self.image = personaje = pygame.image.load(
                "Imagenes/goku.png").convert_alpha()

        if teclas[pygame.K_LEFT]:
            self.image = personaje = pygame.image.load(
                "Imagenes/gokuleft.png").convert_alpha()
            if self.rect.x > 0:
                self.rect.x -= 10
        elif teclas[pygame.K_RIGHT]:
            self.image = personaje = pygame.image.load(
                "Imagenes/gokuright.png").convert_alpha()
            if self.rect.x < 740:
                self.rect.x += 10

        if teclas[pygame.K_UP]:
            self.image = personaje = pygame.image.load(
                "Imagenes/gokuup.png").convert_alpha()
            if self.rect.y > 32:
                self.rect.y -= 10
        elif teclas[pygame.K_DOWN]:
            if self.rect.y < 530:
                self.image = personaje = pygame.image.load(
                    "Imagenes/gokudown.png").convert_alpha()
                self.rect.y += 10


class Kamehameha(pygame.sprite.Sprite):
    def __init__(self):
        self.image = kamehameha = pygame.image.load(
            "Imagenes/kamehameha.gif").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(900, 700)

    def update(self):
        teclas = pygame.key.get_pressed()
        if self.rect.x > 840:
            if teclas[pygame.K_SPACE]:
                self.rect.x = (personaje.rect.x + 60)
                self.rect.y = (personaje.rect.y + 14)
        if self.rect.x < 870:
            self.rect.x += 20


class Barravidagoku(pygame.sprite.Sprite):
    def __init__(self):
        self.image = barravidagoku = pygame.image.load(
            "Imagenes/barravidagoku.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(18, 4)

    def update(self):
        if barravidagoku.rect.x <= -152:
            personaje.muerto = 1
        if disparo.rect.y >= (personaje.rect.y - 56):
            if disparo.rect.y <= (personaje.rect.y + 62):
                if disparo.rect.x >= personaje.rect.x:
                    if disparo.rect.x <= (personaje.rect.x + 43):
                        barravidagoku.rect.x -= 26
                        disparo.rect.x = -400
        if minicell.rect.y >= (personaje.rect.y - 56):
            if minicell.rect.y <= (personaje.rect.y + 62):
                if minicell.rect.x >= personaje.rect.x:
                    if minicell.rect.x <= (personaje.rect.x + 43):
                        barravidagoku.rect.x -= 26
                        disparo.rect.x = -400


class Minicell(pygame.sprite.Sprite):
    def __init__(self):
        self.image = minicell = pygame.image.load(
            "Imagenes/minicell.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(750, 300)
        self.bandera = 0
        self.muerto = 0

    def update(self):
        if self.rect.y == 40:
            self.bandera = 0
        elif self.rect.y == 540:
            self.bandera = 1

        if self.bandera == 0:
            self.rect.y += 10
        elif self.bandera == 1:
            self.rect.y -= 10

    def dificil(self):
        if self.rect.x < 0:
            self.rect.x = 800
        if self.rect.y > 600:
            self.rect.y = 0
        self.rect.x -= 10
        self.rect.y += 10


class Disparo(pygame.sprite.Sprite):
    def __init__(self):
        self.image = barravidagoku = pygame.image.load(
            "Imagenes/disparominicell.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(-400, -400)

    def update(self):
        if self.rect.x == -400:
            if minicell.rect.y == personaje.rect.y:
                self.rect.x = (minicell.rect.x - 60)
                self.rect.y = (minicell.rect.y - 14)
        if self.rect.x > -400:
            self.rect.x -= 5


class Barravidaminicell(pygame.sprite.Sprite):
    def __init__(self):
        self.image = barravidaminicell = pygame.image.load(
            "Imagenes/barravidaminicell.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(612, 4)

    def update(self):
        if self.rect.x >= 782:
            minicell.muerto = 1
        if kamehameha.rect.y >= minicell.rect.y:
            if kamehameha.rect.y <= (minicell.rect.y + 62):
                if kamehameha.rect.x >= minicell.rect.x:
                    if kamehameha.rect.x <= (minicell.rect.x + 43):
                        self.rect.x += 6
                        kamehameha.rect.x = 900


if __name__ == '__main__':
    # Variables.
    salir = False

    # Establezco la pantalla.
    screen = pygame.display.set_mode((800, 600))

    # Establezco el título.
    pygame.display.set_caption("IA enemigo")

    # Creo dos objetos surface.
    fondo = pygame.image.load("Imagenes/pliiiiii.webp").convert()
    cuadrovidagoku = pygame.image.load(
        "Imagenes/cuadrovidagoku.png").convert_alpha()
    cuadrovidaminicell = pygame.image.load(
        "Imagenes/cuadrovidaminicell.png").convert_alpha()
    hasperdido = pygame.image.load("Imagenes/Hasperdido.png").convert()
    hasganado = pygame.image.load("Imagenes/Hasganado.png").convert()
    # .convert() convierten la superficie a un formato de color
    # que permite imprimirlas mucho mas rápido.

    # Objetos
    temporizador = pygame.time.Clock()
    personaje = Personaje()
    kamehameha = Kamehameha()
    minicell = Minicell()
    disparo = Disparo()
    barravidagoku = Barravidagoku()
    barravidaminicell = Barravidaminicell()

    # Movimiento del personaje.
    while not salir:
        personaje.update()
        kamehameha.update()
        if barravidaminicell.rect.x < 697:
            minicell.update()
        else:
            minicell.dificil()
        disparo.update()
        barravidagoku.update()
        barravidaminicell.update()

        # actualizacion grafica
        screen.blit(fondo, (0, 0))
        screen.blit(personaje.image, personaje.rect)
        screen.blit(kamehameha.image, kamehameha.rect)
        screen.blit(minicell.image, minicell.rect)
        screen.blit(disparo.image, disparo.rect)
        screen.blit(barravidagoku.image, barravidagoku.rect)
        screen.blit(barravidaminicell.image, barravidaminicell.rect)
        screen.blit(cuadrovidagoku, (0, 0))
        screen.blit(cuadrovidaminicell, (608, 0))
        if personaje.muerto == 1:
            screen.blit(hasperdido, (250, 264))
        if minicell.muerto == 1:
            screen.blit(hasganado, (250, 264))
        pygame.display.flip()

        if personaje.muerto == 1:
            pygame.time.delay(3000)
            salir = True
        elif minicell.muerto == 1:
            pygame.time.delay(3000)
            salir = True
        temporizador.tick(60)

        # gestion de eventos
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                salir = True
