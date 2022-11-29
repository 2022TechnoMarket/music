import pygame
import time
pygame.init() 


https://user-images.githubusercontent.com/119112927/204473878-041938ae-b1f0-40a0-b8aa-e5b9aea33a7c.mp4



https://user-images.githubusercontent.com/119112927/204473883-6acbafd7-0702-40c9-96bc-4c19dc1c6261.mp4



https://user-images.githubusercontent.com/119112927/204473886-20ed763b-4008-4f1a-b4e2-e955bfb4d1e2.mp4


screen_width = 1240
screen_height = 740
screen = pygame.display.set_mode((screen_width, screen_height))



pygame.display.set_caption("HwanE Game")

background = pygame.image.load("C:\\Users\\송유택\\OneDrive\\바탕 화면\\pymata4-master\\examples\\practice\\888.png")

test_sound1 = pygame.mixer.Sound("C:\\Users\\송유택\\OneDrive\\바탕 화면\\pymata4-master\\examples\\practice\\minigameT11.mp3")

test_sound1.play(-1)

# test_sound2 = pygame.mixer.Sound("C:\\Users\\송유택\\OneDrive\\바탕 화면\\pymata4-master\\examples\\practice\\minigameT2.mp3")

# test_sound2.play(-1)

# test_sound3 = pygame.mixer.Sound("C:\\Users\\송유택\\OneDrive\\바탕 화면\\pymata4-master\\examples\\practice\\GameOver1.mp3")

# test_sound3.play(-1)


 
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
