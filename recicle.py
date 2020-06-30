import pygame
from pygame.locals import *

RED = (255, 0, 0)
WHITE = (255, 255, 255)

class Item(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(x=x, y=y)

    def update(self, rel):
        self.rect.move_ip(rel)

pygame.init()
w, h = 780, 680
display_surface = pygame.display.set_mode((w, h ))
screen = pygame.display.set_mode((w, h))
background = pygame.image.load('background.png')
pygame.display.set_caption("Recicle")

items = pygame.sprite.Group(
    Item("plastico.jpg", 223, 55),
    Item("banana.jpg", 303, 55),
    Item("lata.jpg", 383, 55), 
    Item("papel.jpg", 463, 55),
    Item("garrafa.jpg", 543, 55),
)

dragged = pygame.sprite.Group()

running = True

lixeira_azul = pygame.image.load('lixeira_azul.png')
lixeira_vermelha = pygame.image.load('lixeira_vermelha.png')
lixeira_amarela = pygame.image.load('lixeira_amarela.png')
lixeira_verde = pygame.image.load('lixeira_verde.png')
lixeira_marrom = pygame.image.load('lixeira_marrom.png')

clock = pygame.time.Clock()
game_exit = False

while not game_exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            dragged.add(x for x in items if x.rect.collidepoint(event.pos))          
        elif event.type == pygame.MOUSEBUTTONUP:
            dragged.empty()
        elif event.type == pygame.MOUSEMOTION:
            dragged.update(event.rel)
    
    screen.fill(WHITE)
    screen.blit(background, (0,0))
    items.draw(screen)
    display_surface.blit(lixeira_azul, (20, 510))
    display_surface.blit(lixeira_vermelha, (180, 510))
    display_surface.blit(lixeira_amarela, (340, 510))
    display_surface.blit(lixeira_verde, (520, 510))
    display_surface.blit(lixeira_marrom, (680, 510))
    
    pygame.display.update()

    clock.tick(30)

pygame.quit()
