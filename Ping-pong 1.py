from pygame import *
back =(147, 112, 219)
win_width = 600
win_height = 500
window = display.set_mode((win_width,win_height))
window.fill(back)

clock = time.Clock()
FPS = 60
game = True


class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed, width, height):
        super().__init__()
        self.player_image = player_image
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(player_image),(width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    
    def collidepoint(self,x,y)
        return self.rect.collidepoint(x,y)


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def update_l(self):
            keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def change_img(self,img)
        self.image = transform.scale(image.load(img),(self.width, self.height))

