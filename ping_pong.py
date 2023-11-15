from pygame import *

clock = time.Clock()

font.init()
font1 = font.SysFont('Arial', 36)
lose1 = font1.render('PLAYER 1 LOSE',True,(200,255,200))
lose2 = font1.render('PLAYER 2 LOSE',True,(200,40,100))

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
        if keys[K_UP] and self.rect.y > -20:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > -20:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed

class Balls(GameSprite):
    def update(self):
        self.rect.x += speed_x
        self.rect.y += speed_y

win_width = 900
win_height = 600
display.set_caption('ping_pong')
window = display.set_mode((win_width,win_height))
background = transform.scale(image.load('kfc.jpg'), (900, 600))

player1 = Player('123.png', -10, 350, 100, 200, 10)
player2 = Player('123.png', 800, 350, 100, 200, 10)
ball = Balls('burgar.png', 200, 200, 90, 90, 3)


finish = False

game = True

speed_x = 6
speed_y = 6

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        player1.update_l()
        player2.update_r()
        ball.update()

        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
            speed_y *= 1
        
        if ball.rect.y > win_height - 70 or ball.rect.y < -20:
            speed_y *= -1
        
        if ball.rect.x > win_width - 35:
            finish = True
            window.blit(lose2,(200,200))

        if ball.rect.x < -20:
            finish = True
            window.blit(lose1,(200,200))

        player1.reset()
        player2.reset()
        ball.reset()

    display.update()
    clock.tick(60)
