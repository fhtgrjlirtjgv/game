from pygame import *

#створи вікно гри
window  = display.set_mode((700,500))
FPS = 60
clock = time.Clock()
#задай фон сцени
bg = image.load('background.png')
bg = transform.scale(bg, (700,500))
sp1_img = image.load('sprite1.png')
sp2_img = image.load('sprite2.png')
#створи 2 спрайти та розмісти їх на сцені

class Player(sprite.Sprite):
    def __init__(self, sprite_img, width, height, x , y ):
        self.image = transform.scale(sprite_img, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


sp1_img = Player(sp1_img, 70, 70, 300, 300)
sp2_img = Player(sp2_img, 70, 70, 500, 300)
#оброби подію «клік за кнопкою "Закрити вікно"»
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.blit(bg, (0,0))
    window.blit(sp1_img.image, sp1_img.rect)
    window.blit(sp2_img.image, sp2_img.rect)
    display.update()
    clock.tick(FPS)

