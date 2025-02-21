import pygame
import random
import sys


pygame.init()

# -------------------------------
# 세팅
# -------------------------------
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
pygame.display.set_caption("숫자 지우기 게임")  
clock = pygame.time.Clock()
FPS = 60  
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 128, 255)
RED = (255, 0, 0)
TRANSPARENT_RED = (255, 0, 0, 100)  # 반투명 빨간색 (RGBA)
blocks = []  
drag_start = None  
drag_end = None  
dragging = False  # 드래그 중인지 여부

# -------------------------------
# 게임 로직 및 블록제거 관련
# -------------------------------
def generate_blocks():
    global blocks
    blocks = []
    evenNums = [2,2,2,2,2,4,4,4,6,6,8]
    for i in range(5):  
        for j in range(5):  
            random.shuffle(evenNums)
            num = evenNums[0]
            block = {"rect": pygame.Rect(100 + j*60, 100 + i*60, 50, 50), "value": num}
            blocks.append(block)

def check_drag_selection(start_pos, end_pos):
    selected_blocks = []
    total = 0

    drag_rect = pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]),
                            abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))

    for block in blocks:
        if block["rect"].colliderect(drag_rect):  
            selected_blocks.append(block)
            total += block["value"]

    return selected_blocks, total

def remove_blocks(selected_blocks):
    global blocks
    blocks = [block for block in blocks if block not in selected_blocks]

# -------------------------------
# 게임 종료 조건 : 10의 배수 인가
# -------------------------------
def check_game_clear():
    values = [block["value"] for block in blocks]

    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if (values[i] + values[j]) % 10 != 0:
                return False  
    return True  

def draw_blocks():
    for block in blocks:
        pygame.draw.rect(screen, BLUE, block["rect"])  
        pygame.draw.rect(screen, WHITE, block["rect"], 2)  
        font = pygame.font.Font(None, 36)
        text = font.render(str(block["value"]), True, WHITE)
        screen.blit(text, (block["rect"].x + 15, block["rect"].y + 10))

def draw_drag_area():
    if dragging and drag_start and drag_end:
        drag_rect = pygame.Rect(min(drag_start[0], drag_end[0]), min(drag_start[1], drag_end[1]),
                                abs(drag_end[0] - drag_start[0]), abs(drag_end[1] - drag_start[1]))
        
        overlay = pygame.Surface((drag_rect.width, drag_rect.height), pygame.SRCALPHA)
        overlay.fill(TRANSPARENT_RED)
        screen.blit(overlay, (drag_rect.x, drag_rect.y))

def show_message(text, color=RED):
    font = pygame.font.Font(None, 50)
    message = font.render(text, True, color)
    screen.blit(message, (SCREEN_WIDTH//2 - message.get_width()//2, SCREEN_HEIGHT//2))

# -------------------------------
# 이벤트 처리
# -------------------------------
def handle_mouse_events(event):
    global drag_start, drag_end, dragging

    if event.type == pygame.MOUSEBUTTONDOWN:
        drag_start = event.pos  
        dragging = True  

    elif event.type == pygame.MOUSEMOTION and dragging:
        drag_end = event.pos  

    elif event.type == pygame.MOUSEBUTTONUP:
        drag_end = event.pos  
        dragging = False  

        if drag_start and drag_end:
            selected_blocks, total = check_drag_selection(drag_start, drag_end)
            
            if total % 10 == 0:
                remove_blocks(selected_blocks)  

            if check_game_clear():
                print("게임 클리어!")  

def reset_game():
    generate_blocks()  

# -------------------------------
# 메인 루프
# -------------------------------
def main():
    global running

    reset_game()  
    running = True  

    while running:
        clock.tick(FPS)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                running = False  
            handle_mouse_events(event)  

        screen.fill(WHITE)  
        draw_blocks()  
        draw_drag_area()  

        if check_game_clear():
            show_message("GAME CLEAR!")
            reset_game()

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
