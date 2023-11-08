from pygame import *

clock = time.Clock()


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 1:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 1:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed

win_width = 900
win_height = 600
display.set_caption('ping_pong')
window = display.set_mode((win_width,win_height))
background = transform.scale(image.load('kfc.jpg'), (900, 600))

player1 = Player('123.png', 0, 350, 60, 200, 10)
player2 = Player('123.png', 820, 350, 60, 200, 10)
monster = GameSprite('burgar.png', 200, 200, 90, 90, 3)


finish = False

game = True

speed_x = 3
speed_y = 3

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        player1.update_l()
        player2.update_r()
        monster.update()
        monster.rect.x += speed_x
        monster.rect.y += speed_y


        if sprite.collide_rect(player1, monster) or sprite.collide_rect(player2, monster):
            speed_x *= -1
            speed_y *= 1
        
        if monster.rect.y > win_height-50 or monster.rect.y < 0:
            speed_y *= -1


        player1.reset()
        player2.reset()
        monster.reset()

    display.update()
    clock.tick(60)
