
#음악다운로드
https://user-images.githubusercontent.com/119112927/204474960-c02d29af-d82d-49b8-a255-5ba12a1a5398.mp4
https://user-images.githubusercontent.com/119112927/204474970-8dda56fc-ec01-4857-8ffa-77b624310149.mp4
https://user-images.githubusercontent.com/119112927/204474981-04809b4c-e130-4ae8-969a-2845e079c029.mp4

import pygame
import time
pygame.init() #초기화
#화면 크기 설정
screen_width = 1240 #가로 크기
screen_height = 740 #세로 크기
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
    
    for event in pygame.event.get(): #이벤트의 발생 여부에 따른 반복문
        if event.type == pygame.QUIT: #창을 닫는 이벤트 발생했는가?
            running = False
    screen.blit(background, (0, 0)) #배경에 이미지 그려주고 위치 지정
    pygame.display.update()
    time.sleep(5)
    test_sound1.stop() 
pygame.quit() 



 
  








