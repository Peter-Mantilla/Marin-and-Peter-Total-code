import pygame
from pygame.locals import *
import random as ran

Bxspeed = ran.choice([i for i in range(-10, 11) if i != 0])
Byspeed = ran.choice([i for i in range(-10, 11) if i != 0])
# --------- The Ball Class ---------
class Ball(pygame.sprite.Sprite):
        def __init__(self, x, y, color=(0, 200, 255)):
            super().__init__()
            self.width = 25
            self.height = 25
            self.surf = pygame.Surface((self.width, self.height))
            self.surf.fill(color)
            self.rect = self.surf.get_rect(topleft=(x-12.5, y-30))
            self.speedx = Bxspeed
            self.speedy = Byspeed
        def move (self):
            
            print(ball.rect.x)
            """
            if (ball.rect.x <=5 or ball.rect.x>795):
                print("test one")
                self.Bxspeed = ran.choice([i for i in range(-10, 11) if i != 0])
                self.Byspeed = ran.choice([i for i in range(-10, 11) if i != 0])
                self.rect.centerx = 400
                self.rect.centery = 400
            """ 
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            if pygame.sprite.spritecollideany(ball, paddles):
                print("hit")





# --------- Vertical Paddle Class ---------
class VerticalPaddle(pygame.sprite.Sprite):
    def __init__(self, x, y, color=(0, 200, 255)):
        super().__init__()
        self.width = 25
        self.height = 140
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill(color)
        self.rect = self.surf.get_rect(topleft=(x, y))
        self.speed = 5

    def move(self, keys, controls, screen_width, screen_height):
        if "up" in controls and keys[controls["up"]]:
            self.rect.y -= self.speed
        if "down" in controls and keys[controls["down"]]:
            self.rect.y += self.speed
        if "left" in controls and keys[controls["left"]]:
            self.rect.x -= self.speed
        if "right" in controls and keys[controls["right"]]:
            self.rect.x += self.speed

        # Keep within screen bounds
        self.rect.x = max(0, min(self.rect.x, screen_width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, screen_height - self.rect.height))

# --------- Horizontal Paddle Class ---------
class HorizontalPaddle(pygame.sprite.Sprite):
    def __init__(self, x, y, color=(255, 100, 100)):
        super().__init__()
        self.width = 140
        self.height = 25
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill(color)
        self.rect = self.surf.get_rect(topleft=(x, y))
        self.speed = 5

    def move(self, keys, controls, screen_width, screen_height):
        if "up" in controls and keys[controls["up"]]:
            self.rect.y -= self.speed
        if "down" in controls and keys[controls["down"]]:
            self.rect.y += self.speed
        if "left" in controls and keys[controls["left"]]:
            self.rect.x -= self.speed
        if "right" in controls and keys[controls["right"]]:
            self.rect.x += self.speed

        # Keep within screen bounds
        self.rect.x = max(0, min(self.rect.x, screen_width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, screen_height - self.rect.height))

# --------- Initialize pygame ---------
pygame.init()
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption('User-Controlled Paddles')
font = pygame.font.SysFont(None, 48)
scores = {
    "top": 0,
    "bottom": 0,
    "left": 0,
    "right": 0
}

# --------- Create paddles in center of each screen edge ---------
paddle_top = HorizontalPaddle((screen_width - 140) // 2, 0, (255, 0, 0))                     # Red - Top
paddle_left = VerticalPaddle(0, (screen_height - 140) // 2, (0, 255, 0))                     # Green - Left
paddle_bottom = HorizontalPaddle((screen_width - 140) // 2, screen_height - 25, (0, 0, 255)) # Blue - Bottom
paddle_right = VerticalPaddle(screen_width - 25, (screen_height - 140) // 2, (255, 255, 0))  # Yellow - Right
# --------- Create ball in center of screen ----------------------
ball = Ball((screen_width/2),(screen_height/2),(255,255,255))                                #White - Ball
# --------- Control mapping ---------
controls = {
    paddle_top:    { "left": K_LEFT, "right": K_RIGHT },
    paddle_left:   { "up": K_w, "down": K_s },
    paddle_bottom: { "left": K_j, "right": K_l },
    paddle_right:  { "up": K_t, "down": K_g },
}

paddles = [paddle_top, paddle_left, paddle_bottom, paddle_right]

# --------- Game loop ---------
clock = pygame.time.Clock()
gameOn = True

while gameOn:
    
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_BACKSPACE):
            gameOn = False
        elif event.type == VIDEORESIZE:
            screen_width, screen_height = event.w, event.h
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)


    keys = pygame.key.get_pressed()

    if ball.rect.left < 0:
            scores["left"] += 1
            Bxspeed = ran.choice([i for i in range(-10, 11) if i != 0])
            Byspeed = ran.choice([i for i in range(-10, 11) if i != 0])
            ball.rect.center = (screen_width // 2, screen_height // 2)
    elif ball.rect.right > screen_width:
            scores["right"] += 1
            Bxspeed = ran.choice([i for i in range(-10, 11) if i != 0])
            Byspeed = ran.choice([i for i in range(-10, 11) if i != 0])
            ball.rect.center = (screen_width // 2, screen_height // 2)
    elif ball.rect.top < 0:
            scores["top"] += 1
            Bxspeed = ran.choice([i for i in range(-10, 11) if i != 0])
            Byspeed = ran.choice([i for i in range(-10, 11) if i != 0])
            ball.rect.center = (screen_width // 2, screen_height // 2)
    elif ball.rect.bottom > screen_height:
            scores["bottom"] += 1
            Bxspeed = ran.choice([i for i in range(-10, 11) if i != 0])
            Byspeed = ran.choice([i for i in range(-10, 11) if i != 0])
            ball.rect.center = (screen_width // 2, screen_height // 2)
        # Clear screen
    screen.fill((120,81,169))

    # Move and draw paddles
    for paddle in paddles:
        paddle.move(keys, controls[paddle], screen_width, screen_height)
        screen.blit(paddle.surf, paddle.rect)
    ball.move()
    screen.blit(ball.surf, ball.rect)

    center_x, center_y = screen_width // 2, screen_height // 2

    top_text = font.render(str(scores["top"]), True, (0, 0, 0))
    top_rotated = pygame.transform.rotate(top_text, 180)
    top_rect = top_rotated.get_rect(center=(center_x, center_y - 100))
    screen.blit(top_rotated, top_rect)

    bottom_text = font.render(str(scores["bottom"]), True, (0, 0, 0))
    bottom_rect = bottom_text.get_rect(center=(center_x, center_y + 100))
    screen.blit(bottom_text, bottom_rect)

    left_text = font.render(str(scores["left"]), True, (0, 0, 0))
    left_rotated = pygame.transform.rotate(left_text, 270)
    left_rect = left_rotated.get_rect(center=(center_x - 100, center_y))
    screen.blit(left_rotated, left_rect)

    right_text = font.render(str(scores["right"]), True, (0, 0, 0))
    right_rotated = pygame.transform.rotate(right_text, 90)
    right_rect = right_rotated.get_rect(center=(center_x + 100, center_y))
    screen.blit(right_rotated, right_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
