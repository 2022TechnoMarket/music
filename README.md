import pygame
import time
pygame.init() 

screen_width = 1240
screen_height = 740
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("HwanE Game")

background = pygame.image.load("C:\\Users\\송유택\\OneDrive\\바탕 화면\\pymata4-master\\examples\\practice\\888.png")
test_sound1 = pygame.mixer.Sound("C:\\Users\\송유택\\OneDrive\\바탕 화면\\pymata4-master\\examples\\practice\\minigameT11.mp3")
test_sound1.play(-1)
# test_sound2 = pygame.mixer.Sound("C:\\Users\\송유택\\OneDrive\\바탕 화면\\pymata4-master\\examples\\practice\\minigameT2.mp3")
# test_sound2.play(-1)
# test_sound3 = pygame.mixer.Sound("C:\\Users\\송유택\\OneDrive\\바탕 화면\\pymata4-master\\examples\\practice\\GameOver1.mp3")
# test_sound3.play(-1)

#이벤트 루프
running = True  
while running:
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:  
            running = False
    screen.blit(background, (0, 0)) 
    pygame.display.update()
    time.sleep(5)
    test_sound1.stop() 
pygame.quit()
