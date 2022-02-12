from pygame import *
back =(223,250,142)
win_width = 600
win_height = 500
window = display.set_mode((win_width,win_height))
window.fill(back)

clock = time.Clock()
FPS = 60
game = True
startGame = False
menuOn = False



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
    
    def collidepoint(self,x,y):
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

class Area ():
    def __init__(self, x=y, y=0, width=10, color=(148,218,235))
        self.rect = Rect(x,y,width,height)
        self.fill_color = color
    def color(self,new_color):
        self.fill_color = new_color
    def fill(self):
        draw.rect(window,self.fill_color,self.rect)
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
class Lable(Area):
    def set_text(self,text,fsize = 12, text_color=(75,73,248))
        self.image = pygame.font.SysFont('Times New Roman', fsize).render(texr.True.text_color)
    def draw(self,shift_x = 0,shift_y = 0):
        self.fill()
        window.blit(self.image,(self.rect.x + shift_x, self.rect.y + shift_y))


