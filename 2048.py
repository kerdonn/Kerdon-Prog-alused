import pygame
import random
import sys

# kasutan pygame moodulid Thonnys, et teha enda elu 200x kergemaks
pygame.init()

# dimensioonid
WIDTH, HEIGHT = 400, 500
GRID_SIZE = 4
GRID_WIDTH = 400
GRID_HEIGHT = 400
TILE_SIZE = GRID_WIDTH // GRID_SIZE
BACKGROUND_COLOR = (187, 173, 160)
GRID_COLOR = (205, 193, 180)
FONT_COLOR = (255, 255, 255)
BLACK = (0, 0, 0)

# üles, alla, kõrvale jne
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# nupud millega mängida
KEY_BINDINGS = {
    pygame.K_LEFT: LEFT,
    pygame.K_RIGHT: RIGHT,
    pygame.K_UP: UP,
    pygame.K_DOWN: DOWN
}

# font
FONT = pygame.font.SysFont('clearsans', 40)

# ekraani suurus
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('2048')

# funktsioon mis võtab arvesse terve mängu ala ja jälgib seda
def initialize_grid():
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    return grid

# lisab punkti blokid ekraanile 
def add_new_tile(grid):
    empty_cells = [(x, y) for x in range(GRID_SIZE) for y in range(GRID_SIZE) if grid[x][y] == 0]
    if empty_cells:
        x, y = random.choice(empty_cells)
        grid[x][y] = 2 if random.random() < 0.9 else 4

# joonistab mängu disaini
def draw_grid(grid):
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            pygame.draw.rect(screen, get_tile_color(grid[x][y]), (y * TILE_SIZE, x * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            text = FONT.render(str(grid[x][y]), True, FONT_COLOR)
            screen.blit(text, (y * TILE_SIZE + TILE_SIZE // 2 - text.get_width() // 2,
                               x * TILE_SIZE + TILE_SIZE // 2 - text.get_height() // 2))
    draw_score()

# paar rida mis ilmutavad skoori 
def draw_score():
    score_text = FONT.render("punktid: " + str(score), True, FONT_COLOR)
    screen.blit(score_text, (10, HEIGHT - 40))

# Värvikoodid mis vastavad bloki skoorile (mida kõrgem skoor seda tumedam blokk)
def get_tile_color(value):
    colors = {
        0: (205, 193, 180),
        2: (238, 228, 218),
        4: (237, 224, 200),
        8: (242, 177, 121),
        16: (245, 149, 99),
        32: (246, 124, 95),
        64: (246, 94, 59),
        128: (237, 207, 114),
        256: (237, 204, 97),
        512: (237, 200, 80),
        1024: (237, 197, 63),
        2048: (237, 194, 46),
        4096: (0, 0, 255)  
    }
    return colors[value] if value in colors else (255, 0, 255)

# palju ridu mis võimaldavad mul liigutada noolte nuppudega blokke
def move(grid, direction):
    def move_row(row):
        row = [x for x in row if x != 0]
        while len(row) < GRID_SIZE:
            row.append(0)
        return row

    def merge_row(row):
        global score
        for i in range(GRID_SIZE - 1):
            if row[i] == row[i + 1] and row[i] != 0:
                row[i] *= 2
                row[i + 1] = 0
                score += row[i]
        return row

    def move_left(grid):
        new_grid = []
        for row in grid:
            new_row = move_row(row)
            new_row = merge_row(new_row)
            new_grid.append(move_row(new_row))
        return new_grid

    def move_right(grid):
        reversed_grid = [row[::-1] for row in grid]
        new_grid = move_left(reversed_grid)
        return [row[::-1] for row in new_grid]

    def move_up(grid):
        transposed_grid = [[grid[j][i] for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]
        new_grid = move_left(transposed_grid)
        return [[new_grid[j][i] for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]

    def move_down(grid):
        transposed_grid = [[grid[j][i] for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]
        new_grid = move_right(transposed_grid)
        return [[new_grid[j][i] for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]

    moves = {
        UP: move_up,
        DOWN: move_down,
        LEFT: move_left,
        RIGHT: move_right
    }

    if direction in moves:
        return moves[direction](grid)
    else:
        return grid

# kontrollib kas on "game over" olukord
def is_game_over(grid):
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if grid[x][y] == 0:
                return False
            if x != GRID_SIZE - 1 and grid[x][y] == grid[x + 1][y]:
                return False
            if y != GRID_SIZE - 1 and grid[x][y] == grid[x][y + 1]:
                return False
    return True

# viskab ekraanile "game over" sõnumi kui on vastav olukord
def display_game_over():
    text = FONT.render('sitt lugu lilleke', True, FONT_COLOR)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.wait(2000)

# "game event" funktsioonid
def handle_events(grid):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in KEY_BINDINGS:
                direction = KEY_BINDINGS[event.key]
                new_grid = move(grid, direction)
                if new_grid != grid:
                    add_new_tile(new_grid)
                    draw_grid(new_grid)
                    pygame.display.update()
                    return new_grid
    return grid

# Start screen function
def start_screen():
    screen.fill(BACKGROUND_COLOR)
    # Draw the "Start" button
    start_button_text = FONT.render('Start Game', True, FONT_COLOR)
    start_button_rect = pygame.Rect(WIDTH // 2 - start_button_text.get_width() // 2, HEIGHT // 2 - 50, start_button_text.get_width(), start_button_text.get_height())
    pygame.draw.rect(screen, GRID_COLOR, start_button_rect)
    screen.blit(start_button_text, (WIDTH // 2 - start_button_text.get_width() // 2, HEIGHT // 2 - 50))
    
    pygame.display.update()

    # Event loop for the start screen
    waiting_for_click = True
    while waiting_for_click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    waiting_for_click = False  # Start the game when clicked

# "main" funktsioon mis jooksutab mängu
def main():
    global score
    score = 0
    start_screen()  # Show the start screen

    grid = initialize_grid()
    add_new_tile(grid)
    add_new_tile(grid)
    
    while True:
        screen.fill(BACKGROUND_COLOR)
        draw_grid(grid)
        pygame.display.update()
        if is_game_over(grid):
            display_game_over()
            pygame.quit()
            sys.exit()
        grid = handle_events(grid)

# Jooksutab "main" funktsiooni
if __name__ == '__main__':
    main()
