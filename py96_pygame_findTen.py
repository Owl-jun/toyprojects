import pygame
import random
import sys

# -------------------------------
# 1. Pygame 초기화
# -------------------------------
pygame.init()

# -------------------------------
# 2. 화면 설정 (윈도우 크기, FPS)
# -------------------------------
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
pygame.display.set_caption("숫자 지우기 게임")  
clock = pygame.time.Clock()
FPS = 60  

# -------------------------------
# 3. 색상 정의
# -------------------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 128, 255)
RED = (255, 0, 0)
TRANSPARENT_RED = (255, 0, 0, 100)  # 반투명 빨간색 (RGBA)

# -------------------------------
# 4. 게임 변수 & 객체 설정
# -------------------------------
blocks = []  
drag_start = None  
drag_end = None  
dragging = False  # 드래그 중인지 여부

# -------------------------------
# 5. 블록 생성 함수
# -------------------------------
def generate_blocks():
    """
    게임 시작 시 랜덤한 숫자 블록을 생성하는 함수
    """
    global blocks
    blocks = []
    evenNums = [2,2,2,2,2,4,4,4,6,6,8]
    for i in range(5):  
        for j in range(5):  
            random.shuffle(evenNums)
            num = evenNums[0]
            block = {"rect": pygame.Rect(100 + j*60, 100 + i*60, 50, 50), "value": num}
            blocks.append(block)

# -------------------------------
# 6. 마우스 드래그 감지 및 합 계산 함수
# -------------------------------
def check_drag_selection(start_pos, end_pos):
    """
    마우스 드래그 영역 내의 숫자를 찾아 합을 계산하는 함수
    """
    selected_blocks = []
    total = 0

    drag_rect = pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]),
                            abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))

    for block in blocks:
        if block["rect"].colliderect(drag_rect):  
            selected_blocks.append(block)
            total += block["value"]

    return selected_blocks, total

# -------------------------------
# 7. 블록 제거 함수
# -------------------------------
def remove_blocks(selected_blocks):
    """
    선택한 블록을 삭제하는 함수
    """
    global blocks
    blocks = [block for block in blocks if block not in selected_blocks]

# -------------------------------
# 8. 게임 종료 조건 체크 함수
# -------------------------------
def check_game_clear():
    """
    남은 블록에서 합이 10을 만들 수 있는지 확인하여 게임 종료 조건 체크
    """
    values = [block["value"] for block in blocks]

    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if (values[i] + values[j]) % 10 != 0:
                return False  
    return True  

# -------------------------------
# 9. 블록 그리기 함수
# -------------------------------
def draw_blocks():
    """
    블록을 화면에 그리는 함수
    """
    for block in blocks:
        pygame.draw.rect(screen, BLUE, block["rect"])  
        pygame.draw.rect(screen, WHITE, block["rect"], 2)  
        font = pygame.font.Font(None, 36)
        text = font.render(str(block["value"]), True, WHITE)
        screen.blit(text, (block["rect"].x + 15, block["rect"].y + 10))

# -------------------------------
# 10. 드래그 영역 표시 함수
# -------------------------------
def draw_drag_area():
    """
    드래그한 영역을 반투명한 빨간색으로 표시하는 함수
    """
    if dragging and drag_start and drag_end:
        drag_rect = pygame.Rect(min(drag_start[0], drag_end[0]), min(drag_start[1], drag_end[1]),
                                abs(drag_end[0] - drag_start[0]), abs(drag_end[1] - drag_start[1]))
        
        overlay = pygame.Surface((drag_rect.width, drag_rect.height), pygame.SRCALPHA)
        overlay.fill(TRANSPARENT_RED)
        screen.blit(overlay, (drag_rect.x, drag_rect.y))

# -------------------------------
# 11. 게임 메시지 표시 함수
# -------------------------------
def show_message(text, color=RED):
    """
    게임이 종료되었을 때 메시지를 화면에 표시
    """
    font = pygame.font.Font(None, 50)
    message = font.render(text, True, color)
    screen.blit(message, (SCREEN_WIDTH//2 - message.get_width()//2, SCREEN_HEIGHT//2))

# -------------------------------
# 12. 마우스 이벤트 처리 함수
# -------------------------------
def handle_mouse_events(event):
    """
    마우스 클릭 및 드래그 이벤트를 처리하는 함수
    """
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

# -------------------------------
# 13. 게임 초기화 함수
# -------------------------------
def reset_game():
    """
    게임을 초기화하는 함수
    """
    generate_blocks()  

# -------------------------------
# 14. 메인 게임 루프
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
